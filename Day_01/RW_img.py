import cv2
import os

#Read Image
img_path = os.path.join('..','E','images.jpg')
img = cv2.imread(img_path)

#Write Image
cv2.imwrite(os.path.join('..','30 CV', 'image2.jpg'), img)


#Visiualize Image
cv2.imshow('Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
