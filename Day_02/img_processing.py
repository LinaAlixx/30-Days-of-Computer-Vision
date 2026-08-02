import cv2
import os

#Read Image
img_path = os.path.join('..','E','images.jpg')
img = cv2.imread(img_path)

#### 1. Resize Image
resize_img = cv2.resize(img, (640, 480)) 

#Print Size of Image
print(img.shape)
print(resize_img.shape)

#### 2. Crop Image
cropped_img = img[80:180, 100:200]

# Get the image dimensions
height, width = img.shape[:2]
 
# Define the rotation center
center = (width // 2, height // 2)
 
# Define the rotation angle
angle = 45  # Rotate by 45 degrees
 
# Define the scaling factor
scale = 1.0  # No scaling

#Rotation Matrix
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

#### 3. Rotate Image
rot_img = cv2.warpAffine(img, rot_mat, (width, height))

#Visiualize Images
cv2.imshow('Image', img)
cv2.imshow('Resize Image', resize_img)
cv2.imshow('Cropped Image', cropped_img)
cv2.imshow('Rotated Image', rot_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

