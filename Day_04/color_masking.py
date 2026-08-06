
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

lower = np.array([170, 120, 70])   # أفتح درجة للأزرق
upper = np.array([180, 255, 255]) # أغمق درجة للأزرق

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lower, upper)

#Show images
cv2.imshow('img', img)
cv2.imshow('mask img', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()


