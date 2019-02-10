import cv2
import os

def video_to_frames(video, path_output_dir):

    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) 
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.jpeg') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()
    return count


cou = 273
arr = [[0,0,0,0,0]]
"""cou = video_to_frames('/Users/austin/Desktop/video.mp4', '/Users/austin/Desktop/davis_hack')"""

import argparse
import io
import re
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/austin/Desktop/emotion-detect-123b21293488.json"

from google.cloud import vision
client = vision.ImageAnnotatorClient()


for i in range (0,cou):
        
    with io.open("/Users/austin/Desktop/davis_hack/" + str(i) +".jpeg", 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END vision_python_migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations
    
    for face in faces:
        arr.append([i,face.anger_likelihood,face.joy_likelihood,face.surprise_likelihood,face.sorrow_likelihood])

 





detect_faces(arr)
           
for ar in arr:
        print (ar)
