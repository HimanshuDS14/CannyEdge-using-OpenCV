import cv2
import numpy as np


image = cv2.imread("tom.jpg")


canny = cv2.Canny(image,100,200)

cv2.imshow("canny" , canny)


cv2.imshow("Original" , image)
cv2.waitKey(0)
cv2.destroyAllWindows()