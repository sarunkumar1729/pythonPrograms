import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'sarunkumarvv1993@gmail.com'
receiver_email = 'sarunkumarkmr2000@gmail.com'
subject = 'Subject of the Email'
message = 'This is the message body of the email.'

# Create a message container (MIMEMultipart object)
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message body
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration (for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Use 587 for TLS or 465 for SSL
smtp_username = 'sarunkumarvv1993@gmail.com'
smtp_password = 'tzbv sbaz lxly kjon'

# Create an SMTP connection and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print('Email sent successfully!')
except Exception as e:
    print(f'An error occurred: {str(e)}')
