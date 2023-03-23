import cv2

video = cv2.VideoCapture(0)

if (video.isOpened()== False):
    print("Error al abrir strem de video de la cámara")

while(video.isOpened()):

    ret, frame = video.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)
        cv2.imshow('se te ama. con tecla q te sales', frame)
        k= cv2.waitKey(20)
        # tecla 113 es 'q', de 'quit'
        if k == 113:
            break
    else:
        break
video.release()
cv2.destroyAllWindows()


