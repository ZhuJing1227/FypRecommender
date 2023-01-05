# -*- coding: utf-8 -*-nnnnnnnnnnnnnnnnnnnnnn
"""
@author: abhilash
"""

# importing the required libraries
import os
import sys
import threading
import time

import cv2
import face_recognition
from collections import Counter
# def returnOutput():
# capture the video from default camera
webcam_video_stream = cv2.VideoCapture(0)

smile_cascade = cv2.CascadeClassifier("smile.xml")
SMILE_CASCADE1 = cv2.CascadeClassifier("haarcascade_smile.xml")

# initialize the array variable to hold all face locations in the frame
all_face_locations = []

age = ""
gender = ""
close = False
age_frequency = []
gender_frequency = []

def frequency_table(n, target):
  table = Counter(n)
  counter = 0
  for number in table.most_common():
    if counter < number[1]:
      target = number[0]
      counter = number[1]
      return target


def timer(duration):
    count = 0
    for i in range(duration):
        time.sleep(1)
        count += 1
        print(count)
    global close
    close = True
timer = threading.Thread(target=timer, args=[5])

timer.start()
# def returnOutput():
    # loop through every frame in the video
while True:
    # get the current frame from the video stream as an image
    ret, current_frame = webcam_video_stream.read()
    # resize the current frame to 1/4 size to proces faster
    current_frame_small = cv2.resize(current_frame, (0, 0), fx=0.25, fy=0.25)
    # detect all faces in the image
    # arguments are image,no_of_times_to_upsample, model
    all_face_locations = face_recognition.face_locations(current_frame_small, number_of_times_to_upsample=2,
                                                         model='hog')

    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # looping through the face locations
    for index, current_face_location in enumerate(all_face_locations):
        # splitting the tuple to get the four position values of current face
        top_pos, right_pos, bottom_pos, left_pos = current_face_location
        # change the position maginitude to fit the actual size video frame
        top_pos = top_pos * 4
        right_pos = right_pos * 4
        bottom_pos = bottom_pos * 4
        left_pos = left_pos * 4
        # printing the location of current face
        # print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))

        # Extract the face from the frame, blur it, paste it back to the frame
        # slicing the current face from main image
        current_face_image = current_frame[top_pos:bottom_pos, left_pos:right_pos]

        # The ‘AGE_GENDER_MODEL_MEAN_VALUES’ calculated by using the numpy. mean()
        AGE_GENDER_MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
        # create blob of current flace slice
        # params image, scale, (size), (mean),RBSwap)
        current_face_image_blob = cv2.dnn.blobFromImage(current_face_image, 1, (227, 227), AGE_GENDER_MODEL_MEAN_VALUES,
                                                        swapRB=False)

        # Predicting Gender
        # declaring the labels
        gender_label_list = ['Male', 'Female']
        # declaring the file paths
        gender_protext = "gender_deploy.prototxt"
        gender_caffemodel = "gender_net.caffemodel"
        # creating the model
        gender_cov_net = cv2.dnn.readNet(gender_caffemodel, gender_protext)
        # giving input to the model
        gender_cov_net.setInput(current_face_image_blob)
        # get the predictions from the model
        gender_predictions = gender_cov_net.forward()
        # find the max value of predictions index
        # pass index to label array and get the label text
        gender = gender_label_list[gender_predictions[0].argmax()]



        # draw rectangle around the face detected
        cv2.rectangle(current_frame, (left_pos, top_pos), (right_pos, bottom_pos), (0, 0, 255), 2)

        # display the name as text in the image
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(current_frame, gender , (left_pos, bottom_pos + 20), font, 0.5, (255, 0, 0), 1)
        print( gender)
        gender_frequency.append(gender)
        # smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.9, minNeighbors=20)
        # for x, y, w, h in smile:
        #     smile = cv2.rectangle(current_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # if smile:
            #     webcam_video_stream.release()
            #     cv2.destroyAllWindows()
            #     print(age, gender)




    # showing the current face with rectangle drawn
    cv2.imshow("Webcam Video", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or close:
        break
gender = frequency_table(gender_frequency, gender)


# release the stream and cam
# close all opencv windows open
with  open("coursegender.txt", "w") as file:
    combined= gender
    content = combined
    file.write(content)
file.close()
webcam_video_stream.release()
cv2.destroyAllWindows()


#     return combined
# #
# #
# returnOutput()
