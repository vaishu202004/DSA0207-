import cv2
import numpy as np
# Load images
img1 = cv2.imread("E:/Collection/6107197b4e624e174fd4adb76662b7c5.jpg")
img2 = cv2.imread("E:/Collection/417552160591a2f8f474f05c11c051cf.jpg")
# Define corresponding points
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])
# Estimate projective transformation matrix using DLT
H, _ = cv2.findHomography(pts1, pts2)
# Apply projective transformation to img1
dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
# Display images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
