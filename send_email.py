import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "krisbaker6@gmail.com"
sender_password = "rerb ehuz qvqg pmyk"
receiver_email = "kris.baker5@gmail.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Automated Test Email"

body = "Hey Kris. This is a test email for your automation project"
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