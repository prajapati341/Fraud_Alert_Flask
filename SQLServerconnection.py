import sqlalchemy as sa
import urllib


def set_connction():
    

    params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                    "SERVER=DESKTOP-0UG3I5P;"
                                    "DATABASE=Test;"
                                    "Trusted_Connection=yes")


    engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


    with engine.connect() as con:
        print("connection successful")
        #result=con.execute('select * from airport')
        #print(result.fetchall())