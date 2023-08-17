from googletrans import Translator
from GoogleNews import GoogleNews

translator = Translator()

def getLink(link):
    spos = link.find("https://")
    epos = link.find("&ved=")
    return link[spos:epos]

googlenews = GoogleNews(lang='en', region='US')
googlenews = GoogleNews(period='1d')
googlenews.search('robotic process automation market share')

texts = googlenews.get_texts()
links = googlenews.get_links()

translated = []
for i in range(len(texts)):
    try:
        response = translator.translate(texts[i], src='en', dest='ko')
        translated.append(response.text)
        print("제목: ", response.text)
        print("영문제목: ", texts[i])
        print("링크 : ", getLink(links[i]), "\n")
    except Exception as e:
        print("에러 발생:", str(e))

