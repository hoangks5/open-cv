import imutils
import cv2

image = cv2.imread("image_libary/meo.jpg")

gray_cv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh_binrary = cv2.threshold(gray_cv,127,255,cv2.THRESH_BINARY)
#Conver ảnh theo hàm Threshold

cv2.imshow("ảnh",thresh_binrary)
cv2.waitKey()
cv2.destroyAllWindows()