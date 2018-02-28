import numpy as np
import cv2
import matplotlib.pyplot as plt
from psonic import *
import threading

tx=0.01
seuil=30

capture=cv2.VideoCapture(0)
ret,image=capture.read()
print(image)

previous=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY).astype(np.int16)[::2,::2]
somme_points=previous.shape[0]*previous.shape[1]
print("previous.shape[0] :",previous.shape[0])
print("previous.shape[1] :",previous.shape[1])
x_compare=1
while(capture.isOpened()):
    ret,current_bgr=capture.read()
    if ret:
        current_gray = cv2.cvtColor(current_bgr, cv2.COLOR_BGR2GRAY).astype(np.int16)
        tmp=current_gray[::2,::2]
        print("nb pixel : ",tmp.size)
        result = np.abs(tmp - previous)
        result = np.where(result > seuil, 1, 0).astype(np.uint8)
        previous = np.copy(tmp)
        somme_points_blancs = np.sum(result)
        taux = float(somme_points_blancs) / float(somme_points)
        if taux > tx:

            x, y = np.where(result)
            x_c, y_c = np.mean(x), np.mean(y)

            if (0 < x_c < 80):
                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (108, 0, 46), thickness=-8,
                           lineType=8)
                if(x_compare!=1):
                    play(chord(A3, MINOR), release=0.3)
                    x_compare = 1

            elif (80 < x_c < 160 ):
                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (255, 0, 0), thickness=-8,
                           lineType=8)
                if (x_compare != 2):
                    play(chord(B3, MINOR), release=0.3)
                    x_compare = 2

            elif (160 < x_c < 240):
                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (35, 137, 58), thickness=-8,
                           lineType=8)
                if (x_compare != 3):
                    play(chord(C3, MINOR), release=0.3)
                    x_compare = 3

            elif (240 < x_c < 320):
                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (13, 240, 231), thickness=-8,
                           lineType=8)
                if (x_compare != 4):
                    play(chord(D3, MINOR), release=0.3)
                    x_compare = 4

            elif (320 < x_c < 400):

                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (1, 164, 250), thickness=-8,
                           lineType=8)
                if (x_compare != 5):
                    play(chord(E3, MINOR), release=0.3)
                    x_compare = 5

            else:

                cv2.circle(current_bgr, (int(np.round(y_c)), int(np.round(x_c))), 20, (0, 0, 255), thickness=-8,
                               lineType=8)
                if (x_compare != 6):
                    play(chord(F3, MINOR), release=0.3)
                    x_compare = 6


        cv2.imshow("Video",current_bgr)
        key=cv2.waitKey(8)

        if key==27:
            break
    else:break

capture.release()
cv2.destroyAllWindows()