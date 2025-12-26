#THIS FILE IS FOR SENDING EMAILS

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