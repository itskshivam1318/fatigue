import pandas as pd
from pandas.io.json import json_normalize
from pathlib import Path
import requests
import matplotlib.pyplot as plt

def detect(file_loc):
    subscription_key = "58c00bbdde21416fb4febd2e73d7737d"
    assert subscription_key

    emotion_recognition_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

    header = {'Ocp-Apim-Subscription-Key': subscription_key }

    params = {'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes':'emotion'}

    # Use pathlib to set path to multiple images
    p = Path('./frames/'+file_loc)
    #p = Path('./images')
    # list of all images in dir (use rglob to get subdirectories)
    f = list(p.rglob('*.jpg'))
    print(f)
    data = list()

    # iterate through images
    for face in f:

        image_data = face.open('rb').read()
        headers  = {'Ocp-Apim-Subscription-Key': subscription_key,
                    "Content-Type": "application/octet-stream"}

        response = requests.post(emotion_recognition_url,
                                params=params,
                                headers=headers,
                                data=image_data)

        if response.status_code == 200:
            # parse respone
            data_list = response.json()

            # chcck if the list is empty - happens if api can't process face
            if data_list:
                data_dict = data_list[0]
                # add the file path to dict so you know which is processed
                data_dict['file'] = str(face)
                data.append(data_dict)
            else:
                # add unprocessed face
                data.append({'file': str(face)})
        else:
            response.raise_for_status()

    df = json_normalize(data)
    df.head()
    df.tail()
    print df
    df=df.drop(columns="file")
    df=df.drop(columns="faceId")
    df=df.drop(columns="faceRectangle.top")
    df=df.drop(columns="faceRectangle.left")
    df=df.drop(columns="faceRectangle.width")
    df=df.drop(columns="faceRectangle.height")

    df=df.fillna(0)

    df.loc['sum']=df.sum()
    df.loc['avg']=df.mean()
    sum = df.loc['sum']
    avg = df.loc['avg']
    print(df)
    sum_anger = df.at['sum',"faceAttributes.emotion.anger"]
    avg_anger = df.at['avg',"faceAttributes.emotion.anger"]
    print("anger")
    print(sum_anger,avg_anger)
    sum_contempt = df.at['sum',"faceAttributes.emotion.contempt"]
    avg_contempt = df.at['avg',"faceAttributes.emotion.contempt"]
    print("contempt")
    print(sum_contempt,avg_contempt)
    sum_disgust = df.at['sum',"faceAttributes.emotion.disgust"]
    avg_disgust = df.at['avg',"faceAttributes.emotion.disgust"]
    print("disgust")
    print(sum_disgust,avg_disgust)
    sum_fear = df.at['sum',"faceAttributes.emotion.fear"]
    avg_fear = df.at['avg',"faceAttributes.emotion.fear"]
    print("fear")
    print(sum_fear,avg_fear)
    sum_happiness = df.at['sum',"faceAttributes.emotion.happiness"]
    avg_happiness = df.at['avg',"faceAttributes.emotion.happiness"]
    print("happiness")
    print(sum_happiness,avg_happiness)
    sum_neutral = df.at['sum',"faceAttributes.emotion.neutral"]
    avg_neutral = df.at['avg',"faceAttributes.emotion.neutral"]
    print("neutral")
    print(sum_neutral,avg_neutral)
    sum_sadness = df.at['sum',"faceAttributes.emotion.sadness"]
    avg_sadness = df.at['avg',"faceAttributes.emotion.sadness"]
    print("sadness")
    print(sum_sadness,avg_sadness)
    sum_surprise = df.at['sum',"faceAttributes.emotion.surprise"]
    avg_surprise = df.at['avg',"faceAttributes.emotion.surprise"]
    print("surprise")
    print(sum_surprise,avg_surprise)
    file_loc, avg.plot.bar()
    #plt.show()
    loc='./static/'+file_loc+'.png'
    plt.savefig(loc)
    avg.to_csv('./result/'+file_loc+'.csv')
    return avg
    #plt.close(file_loc)
