import cv2
# Đọc ảnh
image = cv2.imread("image_libary/meo.jpg",cv2.IMREAD_GRAYSCALE) #Màu ảnh
# Show ảnh
cv2.imshow("Ảnh",image)
# Dừng ảnh màn hình
cv2.waitKey()
# Đóng các cửa sổ
cv2.destroyAllWindows()