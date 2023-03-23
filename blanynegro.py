import cv2
import matplotlib.pyplot as plt

img_rec = cv2.imread("img/rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_circ = cv2.imread("img/circle.jpg", cv2.IMREAD_GRAYSCALE)
img_tigre = cv2.imread("img/Tigre.jpg", cv2.IMREAD_COLOR)

#img_bitwise = cv2.bitwise_and(img_rec, img_circ, mask = None)
img_bitwise = cv2.bitwise_not(img_tigre, mask = None)
plt.imshow(img_bitwise, cmap="gray")
plt.show()

plt.figure(figsize=[20,5])
plt.subplot(121); plt.imshow(img_rec, cmap="gray")
plt.subplot(122); plt.imshow(img_circ, cmap="gray")
plt.show()
