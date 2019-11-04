import cv2
import numpy as np
import os
import time
from camera import VideoCamera

def frame(video_no,username):
    FILE_OUTPUT='./videos/'+username+'.mpeg'
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)
    capture_duration = 2
    cap = cv2.VideoCapture(0)
    currentFrame = 0
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'mpeg')
    out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (int(width),int(height)))
    start_time =time.time()
    while(int(time.time() - start_time)<capture_duration):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,1)
            out.write(frame)
            cv2.imshow('frame',frame)
        else:
            break
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
        currentFrame += 1
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # splitting
    cap = cv2.VideoCapture(FILE_OUTPUT)
    try:
        if not os.path.exists('./frames/'+video_no+'/'+username):
            os.makedirs('./frames/'+video_no+'/'+username)
    except OSError:
        print ('Error: Creating directory of data')
    currentFrame = 0
    while(True):
        cap.set(cv2.CAP_PROP_POS_MSEC,(currentFrame*1000))
        ret, frame = cap.read()
        image_last = cv2.imread("frame{}.jpeg".format(currentFrame-1))
        if np.array_equal(frame,image_last):
            break
        name = './frames/'+video_no+'/'+username+'/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
