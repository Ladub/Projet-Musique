## Nouveau code ##

import cv2
import numpy as np
import scipy as sp
from scipy import ndimage

### Capture de la video avec la webcam ###

cap = cv2.VideoCapture(0)
ret, image = cap.read()

### on récupere la première image en niveau de gris ###
previous = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
### on récupere le nombre de points ###
somme_points = previous.shape[0] * previous.shape[1]

### Variable global ###
tx = 0.01
lower_blue = np.array([70, 50, 50])  # teinte basse du bleu
upper_blue = np.array([150, 200, 255])  # teinte haute du bleu

## Pour chaque frame ##
while (1):

    ret, frame = cap.read()  # on récupère la frame

    rond_rouge = cv2.rectangle(frame, (200, 200), (220, 220), (0, 0, 255), thickness=-8,
                            lineType=4)  # on affiche un cercle rouge ( non utilisé pour l’instant mais qui permettra de tester la détection avec un autre rond pour créer un son )

    ## Si le frame est ok ##
    if ret:
        #
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Mask pour récupérer l’image qu’avec les composantes de bleu
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        previous = np.copy(mask)

        # Permet de joindre deux tableaux, et donc de rajouter la couleur sur le mask
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # On cherche à savoir si il y a assez de points bleu
        somme_points_blancs = np.sum(mask)
        taux = float(somme_points_blancs) / float(somme_points)
        if taux > tx:

            x, y = np.where(mask)  ## donne les indices dans le tableau mask du barycentre des points

            x_c, y_c = np.mean(x), np.mean(y)  # donne les coordonnées

            if(x_c>185 and x_c<215 and y_c>185 and y_c<215):



            ##on affiche un point bleu au niveau du barycentre
                cv2.circle(frame, (int(np.round(y_c)), int(np.round(x_c))), 20, (108, 0, 46), thickness=-8,
                       lineType=8)
            """
            connectivity=np.ones((3,3))
            label,nb_labels=sp.ndimage.measurements.label(mask,connectivity)
            hist=np.histogram(label,255)
            list_of_labels=[]


            for i in range(1,len(hist[0])):
                if hist[0][i]>800 : list_of_labels+=[hist[1][i]]

            list_of_connected_components=[]

            for value in list_of_labels:
                image_tmp=np.where(label==value,255,0)
                list_of_connected_components.append(image_tmp)
            print(list_of_labels)
            """

            cv2.imshow('frame', frame)
            cv2.imshow('res', res)

            k = cv2.waitKey(5) & 0xFF
            if k == 5:
                break

cv2.destroyAllWindows()
cap.release()
