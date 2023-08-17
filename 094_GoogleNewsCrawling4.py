from GoogleNews import GoogleNews
import openai

# OpenAI API 키 설정
openai.api_key = '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'

# ChatGPT에 대화 요청 보내기
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # 사용할 엔진 선택
        prompt=message,
        max_tokens=50  # 생성된 문장의 최대 길이 설정
    )
    return response.choices[0].text.strip()

# googlenews = GoogleNews(lang='en', start='08/10/2023', end='08/14/2023')
googlenews = GoogleNews(lang='en', region='US')
googlenews = GoogleNews(period='1d')
googlenews.search('new python packages')
googlenews.results(sort=True)

texts = googlenews.get_texts()
links = googlenews.get_links()

title = []
summary = []
question = None
for i in range(len(texts)):
    print(texts[i], links[i])
    question = f"{texts[i]} 를 한글로 번역해주세요"
    response = send_message(question)
    print("제목: ", response)

    question = f"{links[i]} 를 한글로 요약해주세요"
    response = send_message(question)
    print("내용: ", response)