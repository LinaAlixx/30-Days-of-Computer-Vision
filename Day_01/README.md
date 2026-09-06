# OpenCV Basics: Image and Video Processing 📷🎥

This project contains simple Python scripts demonstrating fundamental Computer Vision tasks using the **OpenCV** library. It covers how to read, display, and save images, as well as how to play video files and capture live webcam feeds.

---

## 🛠️ Prerequisites

Before running the scripts, make sure you have the `opencv-python` library installed. You can install it via your terminal or command prompt using the following command:

```bash
pip install opencv-python
```
---

## 📂 Project Contents
The project includes three main examples:

# 1. Read, Display, and Save Images
This script performs the following tasks:

- Read Image: Loads an image from a specified path using cv2.imread.

- Save Image: Creates a copy of the image and saves it to a new directory using cv2.imwrite.

- Display Image: Opens a window to show the image using cv2.imshow, keeping it open until the user presses any key.
  
> [!NOTE]
> Make sure to update the image paths (img_path and the save location) to match the actual directories on your machine.

<img width="705" height="418" alt="Screenshot 2026-08-01 195058" src="https://github.com/user-attachments/assets/c58c5834-26c7-484a-bd95-187146dfc2bd" />


# 2. Webcam Live Feed
This script opens your computer's default webcam (camera index 0) and displays the live video feed.

Frames are continuously read and displayed inside a while loop.

To stop the camera and close the window, press the q key on your keyboard.

<img width="1366" height="768" alt="Screenshot 2026-08-02 130230" src="https://github.com/user-attachments/assets/64b203da-a5a3-4cdd-8604-c444ff0507eb" />


# 3. Video Playback
This script reads a video file from your local storage and plays it frame by frame.

The video path is passed to the cv2.VideoCapture function.

The video is displayed at a normal speed using cv2.waitKey(40).

> [!NOTE]
> Make sure to replace "videu path" with the actual path of the video file on your computer (e.g., "C:/videos/my_video.mp4").

## 🚀 How to Run
---
- Create a new Python file (e.g., main.py).

- Copy and paste the specific code block you want to test into the file.

- Verify and update the file paths (for images and videos) inside the code.

- Run the script using your IDE or via the terminal:
```bash
python main.py
```
