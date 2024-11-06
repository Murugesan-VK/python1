import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
  
sender_email = "kaviyarasu.c1012@gmail.com"
receiver_email = "vmsvaithigokul2006@gmail.com"
subject = "Login Notification"
message = "Hi friends... How are u?"

smtp_server = "outlook.office365.com"
smtp_port = 587
smtp_username = "kaviyarasu.c1012@gmail.com"
smtp_password = "dotos1012"

email_message = MIMEMultipart()
email_message["From"] = sender_email
email_message["To"] = receiver_email
email_message["Subject"] = subject 

email_message.attach(MIMEText(message, "plain"))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        
        server.login(smtp_username, smtp_password)
                  
        server.send_message(email_message)
        print("Email sent successfully.")
except Exception as e:
    print("An error occurred while sending the email:", str(e))
