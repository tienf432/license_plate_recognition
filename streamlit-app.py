# Python code to read image
import cv2
import pytesseract
import numpy as np
import os
import glob
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread('images/Cars415.png')
print(img.shape) # Print image shape
cv2.imshow("original", img)
cropped_image = img[157:192, 133:261]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

predicted_result = pytesseract.image_to_string(cropped_image, lang ='eng')
print(predicted_result)
path = r'images/Cars415.png'
img = cv2.imread(path, 0)
cv2.imshow('image', img)
predicted_result = pytesseract.image_to_string(img, lang ='eng')
print(predicted_result)
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("Car", img)
# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
