import cv2

image = cv2.imread("image_libary/meo.jpg")

gray_cv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image1 = cv2.Canny(gray_cv,threshold1=20,threshold2=100)
# Tìm cạnh của ảnh

cv2.imshow("ảnh",image1)
cv2.waitKey()
cv2.destroyAllWindows()