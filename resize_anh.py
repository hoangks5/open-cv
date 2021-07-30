import cv2

image = cv2.imread("image_libary/meo.jpg")
cv2.imshow("anh",image)
cv2.waitKey()
# Resize ảnh
image_rz = cv2.resize(image,dsize=(100,200))
cv2.imshow("anh",image_rz)
cv2.waitKey()

cv2.destroyAllWindows()