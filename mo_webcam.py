import cv2
camera_id = 0 # Có thể đọc file video bằng link 'fils/video.avi'
# Mở camera
cap = cv2.VideoCapture(camera_id)
#Đọc ảnh từ camera
while True:
    # Đọc ảnh
    ret, frame = cap.read()
    cv2.imshow("Cam",frame)
    # Đkiện thoát
    if cv2.waitKey(1) & 0xFF == ord('q'): # Bấm Q để thoát Cam
        break

# Giải phóng camera
cap.release()
cv2.destroyAllWindows()