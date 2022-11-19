import pandas as pd
from contextlib import redirect_stderr
#from crypt import methods
from flask import Flask,render_template,request,redirect, url_for,session,flash
import flask
from flask_session import Session
from sqlalchemy import create_engine
import sqlalchemy as sa
import urllib

from sqlalchemy.sql.functions import user
import SQLServerconnection
from markupsafe import escape

#from symbol import pass_stmt


#params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.10.41;DATABASE=Test123;UID=Sa;PWD=Sgpl@123')

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                    "SERVER=DESKTOP-0UG3I5P;"
                                    "DATABASE=Test;"
                                    "Trusted_Connection=yes")

engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))                                    
#engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))                                    


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


Session(app)





@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    

    if request.method=='POST':
        login_result=request.form
        username=login_result['username']
        password=login_result['password']

        with engine.connect() as conn:
            result=conn.execute("select * from login where username=\'{}\' and password=\'{}\'".format(username,password))

            rows1=result.fetchone()
    
            if rows1:
                
                session["username"] = request.form.get("username")

                return redirect(url_for('page2'))  #page2 is function name not html file name
                
            else:
                flash("incorrect username or password")
                return redirect(url_for('home'))   #home is function name not html file name


@app.route("/logout")
def logout():
    session["username"] = "None"
    
    return redirect("/")



@app.route('/page1')
def page1():


    if 'username' in session:
        username=session["username"]

        if username!='None':

            first_name='Sanjay'
            last_name='Prajapati'
            return render_template('Page1.html',first_name=first_name)
        else:
            
            return redirect("/")



@app.route('/page2',methods=['POST','GET'])
def page2():
    
    try:

        if request.method=="POST":
            date_filter=request.form
            fromdt=date_filter['fromdt']
                    
        else:
            pass
    except:
        print("post exception")


    if 'username' in session:
        username=session["username"]
        
        if username !="None":

            conn=engine.connect()
            conn2=engine.connect()
            conn3=engine.connect()

            result=conn.execute("select * from fraud_alert where [Fraud Found] is null order by session_id")
            
            
            result2=conn2.execute("select * from fraud_alert where [Fraud Found] is null")

            todays_done=conn3.execute("select * from fraud_alert where convert(date,sess_start_time)=convert(date,GETDATE()-1) and [Fraud Found] is not null")

            try:


                if fromdt =="":

                    todays_done=conn3.execute("select * from fraud_alert where convert(date,sess_start_time)>=convert(date,GETDATE()-1) and [Fraud Found] is not null")
                    
                else:
                    
                    todays_done=conn3.execute("select * from fraud_alert where convert(date,sess_start_time)='{}' and [Fraud Found] is not null".format(fromdt))
                    
            except:

                todays_done=conn3.execute("select * from fraud_alert where convert(date,sess_start_time)=convert(date,GETDATE()-3) and [Fraud Found] is not null")

                

            
            df=pd.DataFrame(result2)
            df2=pd.DataFrame(todays_done)
            get_cnt=df.shape[0]

            try:
                get_unique_cnt=len(pd.unique(df['session_id']))
            except:
                get_unique_cnt=0




            return render_template('Page2.html',get_result=result.fetchall(),user_session=username,get_cnt=get_cnt,get_unique_cnt=get_unique_cnt,tables=[df2.to_html(classes='data', header="true")])

        else:
            
            return redirect('/')
   
       


@app.route('/update',methods=['POST','GET'])
#app.add_url_rule('/','update','result',methods=['POST','GET'])
def result():

    if request.method=='POST':
        result=request.form
        session_id=result['session_id']
        fraud_session=result['fraud_type']
        investigator=result['investigator']
        Risk_Team_Remarks=result['Risk_Team_Remarks']
        #print(fraud_session)

        with engine.connect() as conn:
            conn.execute("update fraud_alert set [Fraud Found]=\'{}\',Investigator=\'{}\',Risk_Team_Remarks=\'{}\' where session_id={}".format(fraud_session,investigator,Risk_Team_Remarks,session_id))
    return redirect(url_for('page2'))



def session_check():

    if 'username' in session:
        username=session["username"]        
        return "valid"
        
        if username =="None":
            return "None"




app.run(debug=False,host='0.0.0.0')
# if __name__ == "__main__":
#     app.run(debug=True)

