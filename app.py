from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import random
import pandas as pd
import http.client
import requests
import time
import queue
import threading
import multiprocessing
import os
import logging
import numpy as np
import requests
import matplotlib.pyplot as plt
from matplotlib import style
from flask import Flask, request, render_template, redirect, url_for
import ast
from scipy import stats
import scipy as sp
from pandas import DataFrame
import seaborn as sns
import json
from datetime import datetime
import urllib
import statistics
# dummy_data.xlsx

app = Flask(__name__)


import multiprocessing

mpcount = multiprocessing.cpu_count()
import matplotlib.pyplot as plt
with open('logs', 'r') as f:
    lines = f.readlines()
    lines = lines[1:]
    d = [float(line.split()[0]) for line in lines]
    a = [float(line.split()[1]) for line in lines]
    b = [float(line.split()[2]) for line in lines]
    c = [float(line.split()[3]) for line in lines]
    b = [i / mpcount for i in b]


# line chart
labels = [] #df.columns[0:8]
line_values =[]
line_reals =[]


line_values = b
line_reals = c



# end of line chart
values = [30,20,40,80,55,21,71,9]





@app.route('/', methods=("POST", "GET"))
def html_table():
    
    bar_labels=labels
    bar_values=values
    values_real=line_reals
    values_mc=line_values
    
    A=a
    B=b
    C=c
    D=d

    degisken= str(((sum(values_mc) / len(values_mc)),5))  #str(avg(values_mc))
    return render_template('index.html',   title='GPU, CPU and MEMORY usage as TIME SERIES', max=100,
     labelss=bar_labels,
      #values_real=line_reals, values_mc=line_values,
      A = a, B = b, C = c, D = d,
       degisken=degisken )



if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # NO CACHE 
    app.run(debug=True ,host='0.0.0.0')