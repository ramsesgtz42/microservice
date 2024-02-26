import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

if len(sys.argv) < 1:
    print("No recipient email received.")
    exit

# Email configuration
smtp_server = 'smtp.gmail.com' # use this if using gmail
smtp_port = 587  # Gmail's TLS port
sender_email = 'senderemail.com' # sending email goes here
receiver_email = sys.argv[1]    #registered user email here as an argument
password = 'xxxx'  # Your app password

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of the Email' # fill this out how you like

body = 'Thank you for registering!' # fill this out how you like
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Secure the connection
    # Login
    server.login(sender_email, password)
    # Send the email
    server.send_message(message)

print('Email sent successfully') # change or remove this how you like