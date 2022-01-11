

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
import numpy as np
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
# opening the webcam setting up resolution
cap = cv2.VideoCapture(0)  # if you have two webcam just increse the number there is 0,1,2 .....
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detector

detector = HandDetector(detectionCon=0.8, maxHands=1)
# find function for the find the distance
# x is the raw distance y is the value in cm

x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60 ,65, 70, 75,80,85,90,95,100]
coff = np.polyfit(x, y, 2)



# loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        x,y,w, h = hands[0]['bbox']
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]  # there is points numbers  here we use 5 and 17 go to the documentation for the details

        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
        A, B, C = coff
        distanceCM = A*distance**2 + B*distance + C

        print(abs(x2-x1),distanceCM, distance) # this will solve the rotation problem
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x, y))

    cv2.imshow("Image", img)
    cv2.waitKey(1)


