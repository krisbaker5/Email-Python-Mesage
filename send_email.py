import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your email details
sender_email = "youremail@gmail.com"
receiver_email = "recipients_email@gmail.com"
password = "yourpassword"   # Need an app password

# Create the email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Automated Email Subject"  # <-- Add your subject here

# Body of the email
body = "Hi, this is an automated email message!"
message.attach(MIMEText(body, 'plain'))

# Set up the server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server (this is for Gmail)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Log in to the server
    text = message.as_string()  # Convert message to string
    server.sendmail(sender_email, receiver_email, text)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection to the server
