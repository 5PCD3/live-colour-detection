import cv2
import numpy as np

# Define BGR values for different colors
yellow = [0, 255, 255]
red = [0, 0, 255]
green = [0, 255, 0]
blue = [255, 0, 0]
purple = [128, 0, 128]
orange = [0, 165, 255]
gray = [128, 128, 128]

def get_limits(color):
    c = np.uint8([[color]])  # BGR value to convert to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]

    if color == yellow:
        # Adjust the hue range for Yellow color, considering the wrap-around in HSV
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == red:
        # Adjust the hue range for Red color, considering the wrap-around in HSV
        lowerLimit = np.array([159, 50, 70], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == green:
        # Adjust the hue range for Green color, considering the wrap-around in HSV
        lowerLimit = np.array([36, 50, 70], dtype=np.uint8)
        upperLimit = np.array([89, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == blue:
        # Adjust the hue range for Blue color, considering the wrap-around in HSV
        lowerLimit = np.array([90, 50, 70], dtype=np.uint8)
        upperLimit = np.array([128, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == purple:
        # Adjust the hue range for Purple color, considering the wrap-around in HSV
        lowerLimit = np.array([129, 50, 70], dtype=np.uint8)
        upperLimit = np.array([158, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == orange:
        # Adjust the hue range for Orange color, considering the wrap-around in HSV
        lowerLimit = np.array([10, 50, 70], dtype=np.uint8)
        upperLimit = np.array([24, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit

    elif color == gray:
        # Adjust the hue range for Gray color, considering the wrap-around in HSV
        lowerLimit = np.array([0, 0, 40], dtype=np.uint8)
        upperLimit = np.array([180, 18, 230], dtype=np.uint8)
        return lowerLimit, upperLimit

    else:
        return None
