import os
from dotenv import load_dotenv

# This looks for the .env file in the same directory
load_dotenv()

EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def sendEmail():
    # Email Notifications
    # Establish connection to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Secure the connection
        connection.starttls()
        # Login to the email account
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        # Send the email
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,  # Use the email from the CSV file
            msg=f"Subject:Cat Tracker Notification\n\nCat Counter"
        )

    print("Email sent successfully to:", EMAIL)