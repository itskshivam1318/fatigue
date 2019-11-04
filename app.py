from flask import Flask, request, render_template,Response, request,redirect, url_for
import cv2
import numpy as np
import pandas as pd
import os
import time
import json
from camera import VideoCamera
from frame import frame
from flask_executor import Executor
from detect import detect  
import plotly
import plotly.graph_objs as go
from flask import session
from causalimpact import CausalImpact

app = Flask(__name__)

executor = Executor(app)
    #some long running processing here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video1',methods=['GET','POST'])
def video1():
    executor.submit(video1_job)
    return render_template('video1.html')

def video1_job():
    frame("video1","v1out1")
    time.sleep(14)
    frame("video1","v1out2")
    time.sleep(92)
    frame("video1","v1out3")
    time.sleep(1)
    frame("video1","v1out4")
    time.sleep(1)
    frame("video1","v1out5")
    time.sleep(4)
'''    
@app.route("/video1.html",methods=['GET','POST'])
def record():    
    return render_template("video1.html")
'''

@app.route("/video2",methods=['GET','POST'])
def video2():
    executor.submit(video2_job)
    return render_template("video2.html")

def video2_job():
    frame("video2","v2out1")
    time.sleep(14)
    frame("video2","v2out2")
    time.sleep(92)
    frame("video2","v2out3")
    time.sleep(1)
    frame("video2","v2out4")
    time.sleep(1)
    frame("video2","v2out5")
    time.sleep(4)

@app.route("/video3",methods=['GET','POST'])
def video3():
    executor.submit(video3_job)
    return render_template("video3.html")

def video3_job():
    frame("video3","v3out1")
    time.sleep(14)
    frame("video3","v3out2")
    time.sleep(92)
    frame("video3","v3out3")
    time.sleep(1)
    frame("video3","v3out4")
    time.sleep(1)
    frame("video3","v3out5")
    time.sleep(4)

@app.route('/result',methods=['GET', 'POST'])
def result():

    data1 = pd.read_csv(r"./result/video1.csv",names=["emotion","average"])
    anger_avg1 = data1.iloc[0]["average"]
    contempt_avg1 = data1.iloc[1]["average"]
    disgust_avg1 = data1.iloc[2]["average"]
    fear_avg1 = data1.iloc[3]["average"]
    happiness_avg1 = data1.iloc[4]["average"]
    neutral_avg1 = data1.iloc[5]["average"]
    sadness_avg1 = data1.iloc[6]["average"]
    surprise_avg1 = data1.iloc[7]["average"]
    average1= data1.mean()
    
    data2 = pd.read_csv(r"./result/video1.csv",names=["emotion","average"])
    anger_avg2 = data2.iloc[0]["average"]
    contempt_avg2 = data2.iloc[1]["average"]
    disgust_avg2 = data2.iloc[2]["average"]
    fear_avg2 = data2.iloc[3]["average"]
    happiness_avg2 = data2.iloc[4]["average"]
    neutral_avg2 = data2.iloc[5]["average"]
    sadness_avg2 = data2.iloc[6]["average"]
    surprise_avg2 = data2.iloc[7]["average"]
    average2= data2.mean()

    data3 = pd.read_csv(r"./result/video1.csv",names=["emotion","average"])
    anger_avg3 = data3.iloc[0]["average"]
    contempt_avg3 = data3.iloc[1]["average"]
    disgust_avg3 = data3.iloc[2]["average"]
    fear_avg3 = data3.iloc[3]["average"]
    happiness_avg3 = data3.iloc[4]["average"]
    neutral_avg3 = data3.iloc[5]["average"]
    sadness_avg3 = data3.iloc[6]["average"]
    surprise_avg3 = data3.iloc[7]["average"]
    average3= data3.mean()

    return render_template("result.html",anger_avg1=anger_avg1,contempt_avg1=contempt_avg1,disgust_avg1 = disgust_avg1, 
                                        fear_avg1 = fear_avg1,happiness_avg1 = happiness_avg1,neutral_avg1 = neutral_avg1,
                                        sadness_avg1 = sadness_avg1,surprise_avg1 = surprise_avg1,
    
                                        anger_avg2=anger_avg2,contempt_avg2=contempt_avg2,disgust_avg2 = disgust_avg2, 
                                        fear_avg2 = fear_avg2,happiness_avg2 = happiness_avg2,neutral_avg2 = neutral_avg2,
                                        sadness_avg2 = sadness_avg2,surprise_avg2 = surprise_avg2,
    
                                        anger_avg3=anger_avg3,contempt_avg3=contempt_avg3,disgust_avg3 = disgust_avg3, 
                                        fear_avg3 = fear_avg3,happiness_avg3 = happiness_avg3,neutral_avg3 = neutral_avg3,
                                        sadness_avg3 = sadness_avg3,surprise_avg3 = surprise_avg3,
    
                                        average1 = average1,average2 = average2,average3 = average3)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)