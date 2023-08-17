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

html_title = """
<html>
  <body>
    <h4>안녕하세요. RPA Email New 입니다. !</h4>
    <h4>xxx 에 대한 뉴스를 다음과 같이 보내드리오니 참고하세요.</h4>
    <br>
"""

html_body = """
    <h4> 1. RPA 에 대한 뉴스입니다. </h4> 
    <a href=https://daum.net> It's news title</a>
    <br>
"""

html_tail = """
    <br><br>
    <h4>즐거운 하루되시길 바랍니다.</h4>
    <h4>감사합니다.</h4>
    <h4>소혜민 드림.</h4>
  </body>
</html>
"""

html_body = html_title + html_body + html_body + html_tail

message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(html_body, 'html'))

smtp_connection.sendmail(from_email, to_email, message.as_string())
smtp_connection.quit()