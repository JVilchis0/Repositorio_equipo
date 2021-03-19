import cv2
import numpy as np

#cargar la imagen a color
IRGB=cv2.imread('010.jpg')
print(IRGB)
print(IRGB.shape)
print("Lineas agregadas en la rama2")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
cv2.imwrite('IronmanGS.jpg',IGS)
