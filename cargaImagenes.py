import cv2
import numpy as np

#Cargar la imagen a color
IRGB=cv2.imread('imagen.jpg')
print(IRGB)
print(IRGB.shape)
print("Lineas agregadas en la rama2")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
cv2.imwrite('imagenGS.jpg',IGS)

