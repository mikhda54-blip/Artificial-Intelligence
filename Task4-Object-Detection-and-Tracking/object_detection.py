import cv2

# Open webcam
camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    # Show webcam
    cv2.imshow("Object Detection Project", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
camera.release()

cv2.destroyAllWindows()