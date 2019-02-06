from io import BytesIO
import numpy as np
import pandas as pd
import psycopg2
from flask import Flask, render_template,request,send_file, make_response,json
from flask_bootstrap import Bootstrap
from pandas.io.json import json_normalize
from flask_cors import  CORS,cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
Bootstrap(app)
import xgboost as xgb
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
con = psycopg2.connect("dbname=daabi6mhbsu5fm user=ewyivrzjhyxxyy password=dc37c6729bd76a50666bfc9ffad4fa11b6e3a1974834b3b5ab6933f23a25254d host=ec2-54-83-17-151.compute-1.amazonaws.com")
@app.route('/app1',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
  if request.method=='GET':
    try:
      if (isinstance(int(request.args.get('lid')),int) and isinstance(int(request.args.get('mid')),int) and isinstance(int(request.args.get('nid')),int)) == True:
        num1 = request.args.get('lid')
        num2 = request.args.get('mid')
        num3 = request.args.get('nid')
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        cur=con.cursor()
        sql="SELECT auditorid  FROM qms.aud2 where auditorid=%s LIMIT 1"
        cur.execute(sql,([num1]))
        cur1=con.cursor()
        cur2=con.cursor()
        sql1="SELECT siteid  FROM qms.aud2 where siteid=%s LIMIT 1"
        sql2="SELECT deptid  FROM qms.aud2 where deptid=%s LIMIT 1"
        cur1.execute(sql1,([num2]))
        cur2.execute(sql2,([num3]))
        if cur.fetchone()!=None and cur1.fetchone()!=None and cur2.fetchone()!=None:
          print('hello')
                #result = cur.fetchall()
          '''userDetails = request.form
          num1= userDetails['num1']
          num2 = userDetails['num2']
          num3 = userDetails['num3']
          num1 = int(num1)
          num2 = int(num2)
            num3 = int(num3)'''
          num1 = request.args.get('lid')
          num2 = request.args.get('mid')
          num3 = request.args.get('nid')
          num1=int(num1)
          num2=int(num2)
          num3=int(num3)
          sql = """select * from qms.aud2"""
          df = pd.io.sql.read_sql(sql, con)
          DepartmentID = df['deptid']
          AuditorID = df['auditorid']
          SiteID = df['siteid']
          cper = df['cper']
          X = np.array([AuditorID, SiteID, DepartmentID]).T
          y = np.array(cper)
          from sklearn.model_selection import train_test_split
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0)
          abc = AdaBoostRegressor(n_estimators=50,
                                  learning_rate=1)
          model = abc.fit(X_train, y_train)
          z = np.array([num1,num2,num3]).reshape(1, -1)
          # Predict the response for test dataset
          y_pred = model.predict(z)
          y_pred=int(y_pred)
          pythonDictionary = {'a':num1, 'b':num2, 'c':num3,'e':y_pred}
          return  json.dumps(pythonDictionary)
        return 'values entered are out of range'
    except ValueError:
      return 'enter integer type parameters'

   # return render_template('index.html',a=num1,b=num2,c=num3,e=y_pred)
  '''else: 
    sql = """select * from qms.aud2""" 
    df = pd.io.sql.read_sql(sql, con)
    DepartmentID = df['deptid']
    AuditorID = df['auditorid']
    SiteID = df['siteid']
    noofobser = df['noofaber']
    cper = df['cper']
    X = np.array([AuditorID, SiteID, DepartmentID]).T
    y = np.array(cper)
    # Split dataset into training set and test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  # 70% training and 30% test

    # Create adaboost classifer object
    abc = AdaBoostRegressor(n_estimators=50,
                            learning_rate=1)
    # Train Adaboost Classifer
    model = abc.fit(X_train, y_train)
    # Predict the response for test dataset
    y_pred = model.predict(X_test)
    a=np.sqrt(mean_squared_error(y_test, y_pred))
    x = np.array(AuditorID)
    #x = np.append(x, num1)
    x1 = np.array(SiteID)
    #x1 = np.append(x, num2)
    x2 = np.array(DepartmentID)
    #x2 = np.append(x, num3)
    x3 = np.array(noofobser)
    #x3 = np.append(x, num4)
    y1 = np.array(cper)
    y2 = np.append(y, y_pred)
    z = zip(x, x1, x2, y)
    return render_template('index.html', z=z,a=a)

@app.route('/delete')
def user():
    print("")'''
    

