import cv2
import os

"""
    Funtion to convert image to grayscale and apply gaussian blur 
"""
def apply_filter(image_path):

    # Read the image
    frame = cv2.imread(image_path)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Save the filtered image with the same file name
    cv2.imwrite(image_path, res)

__all__ = ['apply_filter']
