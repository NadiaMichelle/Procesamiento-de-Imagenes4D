import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('BTS.jpg', cv2.IMREAD_UNCHANGED)
img_reverso = img[:,:,::-1]
img_YCrCb=cv2.cvtColor(img_reverso,cv2.COLOR_RGB2YCrCb)
img_YUV=cv2.cvtColor(img_reverso,cv2.COLOR_RGB2YUV)

plt.figure(figsize= [10,5])

plt.subplot(2,2,1);plt.imshow(img_reverso);plt.title("BTS en RGB");
plt.subplot(2,2,2);plt.imshow(img_YCrCb);plt.title("BTS en YCrCb");
plt.subplot(2,2,3);plt.imshow(img);plt.title("BTS original");
plt.subplot(2,2,4);plt.imshow(img_YUV);plt.title("BTS en YUV");

plt.show()

