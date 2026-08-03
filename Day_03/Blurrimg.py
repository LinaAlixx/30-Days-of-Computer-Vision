import cv2
import os

#Read Image
img_path = os.path.join('..','E','images.jpg')
img = cv2.imread(img_path)

#Blurring
k = 7
blur_img = cv2.blur(img, (k, k)) 
gaussian_img = cv2.GaussianBlur(img,(k,k), 5)
med_img = cv2.medianBlur(img, k)


#Visiualize Images
cv2.imshow('Image', img)
cv2.imshow('Blur Image', blur_img)
cv2.imshow('Gaussian Blur Image', gaussian_img)
cv2.imshow('Median Blur Image', med_img)
cv2.waitKey(0)

cv2.destroyAllWindows()



