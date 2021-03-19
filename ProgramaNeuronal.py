import numpy as np
import cv2

def convolucion(Ioriginal,Kernel):
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
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

#imagenes
Kernel=1/256*np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,2,1]])

I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#imagenes a numpy arrays
In=np.array(I)


IRGB=cv2.imread('CACC007.jpg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)



#funcion de convolucion
R=convolucion(IGS,Kernel)
print(R)
print(R.shape)
cv2.imwrite('CACC007C.jpg',R)

def maxpooling2(R):
    frm=(len(R)//2)
    crm=(len(R)//2)
    Resultado=np.zeros((frm,crm),np.uint8)
    a=0
    for i in range(0,len(R),2):
        b=0
        for j in range(0,len(R),2):
            Resultado[a][b]=np.amax(R[i:i+2,j:j+2])
            b+=1
        a+=1

    return Resultado

MX = maxpooling2(R)
print(MX)
print(MX.shape)

Kernel2=np.array([[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]])

R2=convolucion(MX,Kernel2)
print(R2)
print(R2.shape)


MX2= maxpooling2(R2)
print(MX2)
print(MX2.shape)
cv2.imwrite('RSB CACC007.jpg',R)







