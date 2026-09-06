# OpenCV Image Smoothing and Blurring Techniques 🌫️

This repository/script demonstrates different techniques for image smoothing (blurring) using the **OpenCV** library in Python. Blurring is a critical preprocessing step in computer vision, commonly used to reduce image noise, remove high-frequency details, and prepare images for further processing like edge detection.

---

## 🛠️ Prerequisites

To run this code, you need to have Python and the `opencv-python` library installed on your system.
```bash
pip install opencv-python
```

---

## 🔍 Types of Blurring Explained

The script applies a `7x7` kernel window (`k = 7`) to the input image using three different blurring algorithms. Here is a detailed breakdown of each type:

### 1. Simple Blur / Averaging (`cv2.blur`)
* **How it works:** It slides a kernel (a matrix) over the image, computes the simple average of all the pixels falling under that kernel area, and replaces the central pixel with this average value.
* **Characteristics:** Fast and straightforward. 
* **When to use it:** Good for basic, uniform smoothing. However, because it treats all pixels equally, it tends to blur the edges of objects in the image quite heavily.

### 2. Gaussian Blur (`cv2.GaussianBlur`)
* **How it works:** Instead of giving equal weight to all pixels under the kernel, it uses a Gaussian function. Pixels located at the center of the kernel are given a higher weight (importance), while pixels further towards the edges of the kernel are given less weight. The `5` in the code represents the standard deviation in the X direction (`sigmaX`).
* **Characteristics:** Produces a more natural-looking blur.
* **When to use it:** Excellent for removing **Gaussian noise** (normal variations in lighting and camera sensors). It performs much better than Simple Blur at smoothing the image while **preserving the edges** of objects.

### 3. Median Blur (`cv2.medianBlur`)
* **How it works:** It takes all the pixel values under the kernel window, sorts them, finds the median (the middle value), and replaces the central pixel with this median value.
* **Characteristics:** Unlike Averaging or Gaussian blur (which can calculate new pixel values that didn't exist in the original image), Median blur always replaces the center pixel with an existing pixel value from the neighborhood.
* **When to use it:** It is extremely effective at removing **Salt-and-Pepper noise** (random isolated white and black pixels scattered across the image). It keeps edges very sharp while entirely eliminating isolated noisy pixels.

---

## 🚀 How to Run

1. Create a new Python file (e.g., `blur_filters.py`) and paste the code into it.
2. Update the `img_path` variable to point to a valid image on your machine (e.g., `images.jpg`).
3. Run the script from your terminal:
   ```bash
   python blur_filters.py
   ```
4. Four windows will appear showing the results side-by-side:
   * Original Image
   * Blur Image (Averaging)
   * Gaussian Blur Image
   * Median Blur Image

     <img width="631" height="693" alt="Screenshot 2026-08-03 215728" src="https://github.com/user-attachments/assets/12a71636-c584-4427-9a7c-b31d706783bb" />

5. Press any key on your keyboard while the windows are focused to close them and terminate the script.
