# OpenCV Basics: Image and Video Processing 📷🎥

This project contains simple Python scripts demonstrating fundamental Computer Vision tasks using the **OpenCV** library. It covers how to read, display, and save images, as well as how to play video files and capture live webcam feeds.

---

## 🛠️ Prerequisites

Before running the scripts, make sure you have the `opencv-python` library installed. You can install it via your terminal or command prompt using the following command:

```bash
pip install opencv-python
```
## ⚙️ Features & Operations
This script performs the following core image processing tasks on a single image:

# 1. Resizing Images (Scaling)
Changes the dimensions of the original image to a specific width and height (e.g., 640x480) using cv2.resize.

Prints the shape (dimensions) of both the original and the resized images to the console to show the difference.



# 2. Cropping Images (Region of Interest)
Extracts a specific portion of the image using NumPy slicing.

In this example, it cuts out the region from the y-coordinates 80 to 180 and the x-coordinates 100 to 200.


# 3. Rotating Images
Calculates the center of the image to use it as the pivot point.

Generates a 2D rotation matrix using cv2.getRotationMatrix2D with a specific angle (e.g., 45 degrees) and scaling factor.

Applies the affine transformation using cv2.warpAffine to output the rotated image without cropping its corners (based on the original canvas size).

4. Visualization
Opens multiple windows simultaneously to display the results side-by-side:

- Original Image
<img width="377" height="356" alt="Screenshot 2026-08-01 195058" src="https://github.com/user-attachments/assets/6f436520-4a12-46f9-8d7f-1af075163254" />


- Resized Image
<img width="989" height="591" alt="Screenshot 2026-08-02 215254" src="https://github.com/user-attachments/assets/94e35684-5ae9-4f59-b515-1d11043f45da" />

- Cropped Image
<img width="647" height="400" alt="Screenshot 2026-08-02 221619" src="https://github.com/user-attachments/assets/04f8b2ae-deef-4cca-969c-3429c4609ead" />

- Rotated Image
  <img width="774" height="399" alt="Screenshot 2026-08-02 222544" src="https://github.com/user-attachments/assets/98d8d038-dd88-4774-b253-9be59f28c5c9" />


Waits for the user to press any key before safely closing all windows.

## 🚀 How to Run
- Create a new Python file (e.g., transformations.py) and paste the code into it.

- Update the img_path variable to point to a valid image on your machine (e.g., images.jpg).

- Run the script from your terminal:

'''Bash
python transformations.py
'''
- Press any key on your keyboard while the image windows are in focus to close them and exit the program.
