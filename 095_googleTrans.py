from googletrans import Translator

# Translator 객체 생성
translator = Translator()

# 번역할 텍스트
text_to_translate = "Hello, how are you?"

try:
    # 번역
    translated_text = translator.translate(text_to_translate, src='en', dest='ko')

    # 번역 결과 출력
    print("원본 문장:", text_to_translate)
    print("번역 결과:", translated_text.text)
except Exception as e:
    print("에러 발생:", str(e))
