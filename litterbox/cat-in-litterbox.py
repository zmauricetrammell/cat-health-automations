import cv2
import smtplib

import os
from dotenv import load_dotenv

# This looks for the .env file in the same directory
load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

def sendEmail():
    # TODO: Write send email function
    MY_EMAIL = ""
    MY_PASSWORD = ""
    # Email Notifications
    # Establish connection to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Secure the connection
        connection.starttls()
        # Login to the email account
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        # Send the email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,  # Use the email from the CSV file
            msg=f"Subject:Cat Tracker Notification\n\nCat Counter"
        )

    print("Email sent successfully to:", MY_EMAIL)
    
cap = cv2.VideoCapture(0)

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


<<<<<<< HEAD

# Email Notifications
# Establish connection to the Gmail SMTP server
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # Secure the connection
    connection.starttls()
    # Login to the email account
    connection.login(user=username, password=password)
    # Send the email
    connection.sendmail(
        from_addr=username,
        to_addrs=username,
        msg=f"Subject:Cat Tracker Notification\n\nCat Counter"
    )

print("Email sent successfully to:", username)
=======
>>>>>>> b4bf75886d4720f006da2320e15d3ff046d089ee
