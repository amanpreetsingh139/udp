# import cv2
# # RTSP_URL = f"rtsp://{USERNAME}:{PASSWORD}@192.168.1.221:554/11"
# video = cv2.VideoCapture("http://100.74.14.194:/playlist.m3u")
# while True:
#     ret, frame = video.read()
#     cv2.imshow("RTSP", frame)
#     k = cv2.waitKey()
#     if k == ord('q'):
#         break
#
# video.release()
# cv2.destroyAllWindows()
import cv2
#cap = cv2.VideoCapture("rtsp://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream")
cap = cv2.VideoCapture("rtsp://localhost:8554/mystream")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()