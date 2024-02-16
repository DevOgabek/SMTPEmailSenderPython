import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

def send_email(sender_email, sender_password, receiver_email, subject, message):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    server.quit()

sender_email = EMAIL
sender_password = PASSWORD
receiver_email = 'oavazov014@gmail.com'  
subject = 'Subject of the email'
message = 'Body of the email'

send_email(sender_email, sender_password, receiver_email, subject, message)