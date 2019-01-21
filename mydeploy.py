from io import BytesIO
import pandas as pd
from flask import Flask,render_template
import psycopg2
import numpy as np
app = Flask (__name__)
con = psycopg2.connect("dbname=dfhaphi9vtlee6 user=qcmezkrwpidutn password=3fd32869bc0d2fb997e2c47dfe339f552267e7c40bc00949638ae3b43947a64d host=ec2-107-20-183-142.compute-1.amazonaws.com")
@app.route('/')
def index():
  sql = """select * from qms.aud2"""
  df = pd.io.sql.read_sql(sql, con)
  DepartmentID = df['deptid']
  AuditorID = df['auditorid']
  x1 = np.array(AuditorID)
  x2 = np.array(DepartmentID)
  z = zip(x, x1, x2, x3, y)
  return render_template('index.html', z=z)
