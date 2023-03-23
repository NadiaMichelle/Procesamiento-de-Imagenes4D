import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('BTS.jpg',cv2.IMREAD_UNCHANGED) #CARGA LA IMAGEN SIN CAMBIOS
img_gris = cv2.imread('BTS.jpg',cv2.IMREAD_GRAYSCALE)
retval, img_tresh = cv2.threshold(img_gris, 100, 255, cv2.THRESH_BINARY)

img_reverso = img[:,:,::-1]# INVIERTE LOS COLORES A RGB, ORIGINALMENTE ES BGR
#img_YCrCb = cv2.cvtColor(img_reverso,cv2.COLOR_RGB2YCrCb)
img_YUV = cv2.cvtColor(img_reverso,cv2.COLOR_RGB2YUV) 

matrix3 = (30,30)
matrix1 = np.ones(img_reverso.shape)*.5
matrix2 = np.ones(img_reverso.shape)*1.5
#filtros
#img_oscura = np.uint8(cv2.multiply(np.float64(img_reverso),matrix1))
#img_clara = np.uint16(cv2.multiply(np.float64(img_reverso),matrix2))
img_borrosa = cv2.blur(img_reverso, matrix3)

plt.figure(figsize=[5,5])
#          rows, cols, num
plt.subplot(2, 2, 1);plt.imshow(img_reverso);plt.title('BTS en RGB');
plt.subplot(2, 2, 2);plt.imshow(img_borrosa);plt.title('BTS en borroso');
plt.subplot(2, 2, 3);plt.imshow(img_gris, cmap="gray");plt.title('BTS Oscura');
plt.subplot(2, 2, 4);plt.imshow(img_tresh, cmap="gray");plt.title('BTS con umbral');


plt.show()
