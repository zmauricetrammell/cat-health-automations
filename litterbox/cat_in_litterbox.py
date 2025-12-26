import cv2
from email_sender.send_email import sendEmail

cap = cv2.VideoCapture(0)

CAT_THRESHOLD = 300

HEIGHT = 480
WIDTH = 640

cat_instance = 0

if not cap.isOpened():
    print("Error: Could not open video device or file")
    exit()

while True:
    # Read a frame from the video source
    ret, frame = cap.read()

    # Check if frame is there
    if not ret:
        print("End of video or error reading frame." )
        break

    # Draw red crosshair in center
    cv2.line(frame, (320-10,240), (320-2,240),(0,0,255),1)
    cv2.line(frame, (320+2,240), (320+10,240),(0,0,255),1)
    cv2.line(frame, (320,240-10), (320,240-2),(0,0,255),1)
    cv2.line(frame, (320,240+2), (320,240+10),(0,0,255),1)

    # Check center pixels for color
    bgr_color = frame[240, 320]
    
    if bgr_color[0] < 75 and bgr_color[1] < 75 and bgr_color[2] < 75:
        cat_instance += 1    
        print("CAT")
        if cat_instance >= CAT_THRESHOLD:
            print("CAT IN LITTERBOX")
            sendEmail()
            cat_instance = 0
    else:
        cat_instance = 0
        print("NO CAT")

    # Display the frame in a window named USB Camera
    cv2.imshow('USB Camera', frame)

    # Press 'q' tp exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video source and close all OpenCV Windows
cap.release()
cv2.destroyAllWindows()