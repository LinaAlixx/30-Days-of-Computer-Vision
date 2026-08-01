import cv2

#Read Video
vid = cv2.VideoCapture(r"videu path")

#Visiualize Video
ret = True
while ret:
    ret, frame = vid.read()

    if ret:
        cv2.imshow('Frame', frame)
        cv2.waitKey(40)

vid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
