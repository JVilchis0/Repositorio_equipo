import numpy as np
import cv2

def convolucion(Ioriginal,Kernel):
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #For para recorrer filas
    for i in range(len(Resultado)):
        for j in range(len(Resultado[0])):
            suma=0
            #hace las multiplicaciones y las suma
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*Ioriginal[m+i][n+j]
            if suma<=255:
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado
#imagen artificial
K=[[-1,0,1],[-1,0,1],[-1,0,1]]
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#imagenes a numpy array
In=np.array(I)
Kn=np.array(K)

IRGB=cv2.imread('Ironman.jpg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#funcion de convolucion
R=convolucion(IGS,Kn)
print(R)
print(R.shape)
cv2.imwrite('IronmanC.jpg',R)

#Max-pooling
def maxpooling2(R):
    frm=len(R)//2
    crm=len(R[0])//2
    Resultado=np.zeros((frm,crm),np.uint8)
    
