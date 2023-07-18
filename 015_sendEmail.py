import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the connection to the SMTP server
smtp_server = 'smtp.naver.com'
smtp_port = 587
smtp_username = 'rickykwak@naver.com'
smtp_password = 'Autoban00@'
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.ehlo()
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Define the email message
from_email = 'rickykwak@naver.com'
to_email = 'sohyemini@gmail.com'
subject = 'Test HTML email'

html_body = """
<html>
  <body>
    <h1>This is a test HTML email sent using Python!</h1>
    <p>You can use HTML tags to format your message.</p>
  </body>
</html>
"""

message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(html_body, 'html'))

# Send the email
smtp_connection.sendmail(from_email, to_email, message.as_string())

# Close the connection to the SMTP server
smtp_connection.quit()