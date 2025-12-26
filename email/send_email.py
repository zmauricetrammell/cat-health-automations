from environment import EMAIL_USERNAME as EMAIL
from environment import EMAIL_PASSWORD as EMAIL_PASSWORD

import smtplib


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

