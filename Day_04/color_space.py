import cv2
import numpy as np
import urllib.request

#Image from internet
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScOyCGA51PlWxddHZLwfFt_arRYEdeRAkImUGtkyOeiQ&s=10"

# Read image from URL
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

# Transform image to array 
img = cv2.imdecode(arr, -1)

#Color Spaces
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#Show images
cv2.imshow('img', img)
cv2.imshow('RGB img', img_rgb)
cv2.imshow('HSV img', img_hsv)
cv2.imshow('Gray img', img_gray)
cv2.imshow('lab img', img_lab)

cv2.waitKey(0)
cv2.destroyAllWindows()



