import cv2
import os


def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.jpeg') %
                        count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()
    return count


import argparse
import io
import re
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "emotion-detect-123b21293488.json"


def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_face_detection]
    # [START vision_python_migration_image_file]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END vision_python_migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    for face in faces:
        print(face.anger_likelihood, "    ", face.joy_likelihood, "   ",
              face.surprise_likelihood, "     ", face.sorrow_likelihood)


print("image num       anger       joy      surprice     sorrow")

cou = 3
for i in range(0, cou):
    detect_faces("/test/" + str(i) + ".jpg")
