from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import psycopg2
import xgboost as xgb
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
import pygal
plt.style.use('ggplot')
app = Flask(__name__)
Bootstrap(app)
con = psycopg2.connect("dbname=dfhaphi9vtlee6 user=qcmezkrwpidutn password=3fd32869bc0d2fb997e2c47dfe339f552267e7c40bc00949638ae3b43947a64d host=ec2-107-20-183-142.compute-1.amazonaws.com")
@app.route('/')
def index():
  sql = """select * from qms.aud2"""
  df = pd.io.sql.read_sql(sql, con)
  DepartmentID = df['deptid']
  AuditorID = df['auditorid']
  x1 = np.array(AuditorID)
  x2 = np.array(DepartmentID)
  z = zip(x1, x2)
  return render_template('index.html', z=z)
