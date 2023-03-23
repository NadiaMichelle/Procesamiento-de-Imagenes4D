import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/Monumento.jpg')

img_blur = cv2.blur(img, (10,10))
img_median = cv2.medianBlur(img,5)
img_gauss = cv2.GaussianBlur(img,(5,5),0)
img_bilateral = cv2.bilateralFilter(img,9,75,75)
img_laplaciano = cv2.Laplacian(img_gauss, cv2.CV_64F)
img_laplaciano_b = img_laplaciano/img_laplaciano.max()

plt.figure(figsize=[10,5])
plt.subplot(221);plt.imshow(img)
plt.subplot(222);plt.imshow(img_gauss)
plt.subplot(223);plt.imshow(img_bilateral)
plt.subplot(224);plt.imshow(img_laplaciano_b)
plt.show()