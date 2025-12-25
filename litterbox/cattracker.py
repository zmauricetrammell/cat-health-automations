import cv2

def sendEmail():
    # TODO: Write send email function
    print('send email')
    
cap = cv2.VideoCapture(1)

HEIGHT = 480
WIDTH = 640

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
    
    if bgr_color[0] < 100 and bgr_color[1] < 100 and bgr_color[2] < 100:
        # TODO: Send notification if cat is in litter box
        sendEmail()
        print("CAT")
    else:
        print("NO CAT")

    # Display the frame in a window named USB Camera
    cv2.imshow('USB Camera', frame)

    # Press 'q' tp exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video source and close all OpenCV Windows
cap.release()
cv2.destroyAllWindows()

