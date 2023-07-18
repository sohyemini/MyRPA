import openai

# OpenAI API 키 설정
openai.api_key = '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'


# ChatGPT에 대화 요청 보내기
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  # 사용할 엔진 선택
        prompt=message,
        max_tokens=100,  # 응답으로 받을 토큰 수 설정
        temperature=0.7,  # 다양성 조절을 위한 온도 설정
        n=1,  # 몇 개의 응답을 받을지 설정
        stop=None,  # 대화를 멈출 토큰 설정 (None일 경우, 모델이 알아서 멈춤)
        # log_level='info'  # 로그 레벨 설정
    )
    return response.choices[0].text.strip()


# 대화 반복
print("ChatGPT를 시작합니다. '종료'를 입력하면 대화가 종료됩니다.")

while True:
    user_input = input("사용자: ")

    if user_input == '종료':
        print("ChatGPT를 종료합니다.")
        break

    response = send_message(user_input)
    print("ChatGPT: ", response)
