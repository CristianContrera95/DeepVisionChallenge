"""
__author__ = Cristian Contrera
__email__ = cristiancontrera95@gmail.com
__date__ = 15/10/2019
"""


import sys
import os
import cv2
import numpy as np
from nms import nms


# created if not exits an output folder
try:
    os.mkdir('output')
except:
    pass
output_folder = os.path.join(os.path.abspath(os.curdir), 'output')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('there aren\'t args')
        exit(1)

    overlapThresh = float(sys.argv[-1])
    images_folder = os.path.join(os.path.abspath(os.curdir), sys.argv[1])

    haar_cascades = [
        'haarcascade_frontalface_default.xml',
        'haarcascade_profileface.xml',
    ]

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_cascades[0])
    face_profile = cv2.CascadeClassifier(cv2.data.haarcascades + haar_cascades[1])

    for img_path in os.listdir(images_folder):
        image = cv2.imread(os.path.join(images_folder, img_path))
        image_ = image.copy()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces_front = face_cascade.detectMultiScale(image_gray, 1.1, 4)
        faces_profile = face_profile.detectMultiScale(image_gray, 1.1, 4)

        faces = np.concatenate([f for f in [faces_front, faces_profile] if len(f)>0])
        for (x, y, w, h) in faces:
            cv2.rectangle(image_, (x, y), (x+w, y+h), (0, 0, 255), 2)
            # Add fake rectangles
            cv2.rectangle(image_, (x+5, y+3), (x+w+5, y+h+10), (0, 255, 0), 2)   
            cv2.rectangle(image_, (x, y+2), (x+w+3, y+h+8), (0, 255, 0), 2)    

        cv2.imwrite(f'{output_folder}/{img_path.split(".")[0]}_pre_nms.jpg', image_)

        faces = nms(faces, overlapThresh)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imwrite(f'{output_folder}/{img_path.split(".")[0]}_post_nms.jpg', image)
