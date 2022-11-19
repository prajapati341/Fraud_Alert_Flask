from contextlib import redirect_stderr
#from crypt import methods
from flask import Flask,render_template,request,redirect, url_for,session
import sqlalchemy as sa
import urllib
import SQLServerconnection
from markupsafe import escape
# http://localhost:5000/python/logout - this will be the logout page


app = Flask(__name__)

@app.route('/Flask/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   print("logout")
   # Redirect to login page
   return redirect(url_for('login'))