import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"
sender_password = "your app password"
receiver_email = "receiver_email@example.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Automated Test Email"

body = "Hey there! This is a test email sent from a Python Project!"
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent sucessfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
