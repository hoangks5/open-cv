import cv2

image = cv2.imread("image_libary/meo.jpg")

gray_cv = cv2.cvtColor(image,0)

image1 = cv2.GaussianBlur(gray_cv,ksize=(15,35),sigmaX=0) #kzise(số lẻ,số lẻ)
#ksize càng lớn ảnh càng mờ

cv2.imshow("ảnh",image1)
cv2.waitKey()
cv2.destroyAllWindows()