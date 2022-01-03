# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setti

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
import cv2
from cvzone.HandTrackingModule import HandDetector
# opening the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detector

detector = HandDetector(detectionCon=0.8, maxHands=1)

# loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]  # there is points numbers  here we use 5 and 17 go to the documentation for the details

        distance= math.sqrt((y2-y1)**2 + (x2-x1)**2)

        print(abs(x2-x1), distance) # this will solve the rotation problem

    cv2.imshow("Image", img)
    cv2.waitKey(1)

#check commit