from googletrans import Translator
from GoogleNews import GoogleNews
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class RPANewsEmailer():

    def __init__(self):
        self.translator = Translator()
        self.googlenews = GoogleNews(lang='en', region='US')
        self.googlenews = GoogleNews(period='1d')

        self.smtp_server = 'smtp.naver.com'
        self.smtp_port = 587

        self.to_email = []
        self.title_translated = []
        self.subject = None
        self.html = None

    def emailServerLogin(self, username, password):
        self.smtp_username = username
        self.smtp_password = password
        self.smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.smtp_connection.ehlo()
        self.smtp_connection.starttls()
        self.smtp_connection.login(self.smtp_username, self.smtp_password)

    def emailReceiver(self, receivers):
        self.to_email = receivers

    def setEmailSubject(self, sub):
        self.subject = sub

    def setEmailHeader(self, search):
        self.html = None
        html_title = f"""
        <html>
          <body>
            <h4>안녕하세요. RPA Email New 입니다. !</h4>
            <h4>{search} 에 대한 뉴스를 다음과 같이 보내드리오니 참고하세요.</h4>
            <br>
        """
        self.html = html_title
    def addEmailBody(self, i, trans, addr, eng_title):
        html_body = f"""
            <h4>{i}. {trans}. </h4> 
            <a href={addr}>{eng_title}</a>
            <br>
        """
        self.html += html_body

    def setEmailTail(self, sender):
        html_tail = f"""
            <br>
            <h4>즐거운 하루되시길 바랍니다.</h4>
            <h4>감사합니다.</h4>
            <h4>{sender} 드림.</h4>
          </body>
        </html>
        """
        self.html += html_tail

    def sendEmail(self):
        message = MIMEMultipart()
        message['From'] = self.smtp_username
        message['To'] = ', '.join(self.to_email)
        message['Subject'] = self.subject
        message.attach(MIMEText(self.html, 'html'))

        self.smtp_connection.sendmail(self.smtp_username, self.to_email, message.as_string())

    def smtpConnectionQuit(self):
        self.smtp_connection.quit()

    def getLink(self, link):
        spos = link.find("https://")
        epos = link.find("&ved=")
        return link[spos:epos]

    def newsCrawling(self, keyword):
        self.googlenews.search(keyword)
        self.title_texts = self.googlenews.get_texts()
        self.links = self.googlenews.get_links()
        self.title_translated.clear()

        self.setEmailHeader(keyword)
        for i in range(len(self.title_texts)):
            try:
                response = self.translator.translate(self.title_texts[i], src='en', dest='ko')
                self.title_translated.append(response.text)
                print("제목: ", self.title_translated[i])
                print("영문제목: ", self.title_texts[i])
                print("링크 : ", self.getLink(self.links[i]), "\n")
                self.addEmailBody(i+1, self.title_translated[i], self.getLink(self.links[i]), self.title_texts[i])
            except Exception as e:
                print("에러 발생:", str(e))
        self.setEmailTail('소혜민')

if __name__ == "__main__":
    rpa = RPANewsEmailer()
    rpa.emailServerLogin('rickykwak@naver.com', 'Autoban00@')
    receiver = ['ricky.kwak@gmail.com', 'sohyemini@gmail.com']
    rpa.emailReceiver(receiver)
    rpa.setEmailSubject('Daily Email News')
    rpa.newsCrawling('Electric Vehicle safety')
    rpa.sendEmail()