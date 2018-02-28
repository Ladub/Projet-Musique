import cv2

import matplotlib.pyplot as plt
import numpy as np
import math

def histo(image,couleur):
    bins= np.arange(np.min(image), np.max(image) + 1)  # abscisse
    histo = np.zeros((len(bins)))  # ordonnée
    for i in image:
        for j in i:
            histo[j[couleur] - bins[0]] += 1
    return(bins,histo)

img1 = cv2.imread("D:\spiderman_test.jpg")
red,green,blue = cv2.split(img1)
print(red)
seuil=80
ret,seg_red = cv2.threshold(red,seuil,0,cv2.THRESH_BINARY_INV)
plt.figure(figsize=(4,4))
cv2.imshow("seg_red",seg_red)


plt.plot(histo(img1,2)[0],histo(img1,2)[1])
plt.show()
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()