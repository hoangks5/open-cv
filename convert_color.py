import cv2

image = cv2.imread("image_libary/meo.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("same.png", image) # Lưu file ảnh mới

##################################################

image1 = cv2.imread("meo.jpg")
cv2.imshow("anh",image1)
cv2.waitKey()
image_conver = cv2.cvtColor(image1, cv2.COLOR_BGR2RGBA) # Convert màu
cv2.imshow("meo",image_conver)
cv2.waitKey()
cv2.destroyAllWindows()