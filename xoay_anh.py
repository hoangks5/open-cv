import imutils
import cv2

image = cv2.imread("image_libary/meo.jpg")
image_rotate = imutils.rotate(image,90) # Xoay ảnh 90 độ
cv2.imshow("ảnh",image_rotate)
cv2.waitKey()
cv2.destroyAllWindows()