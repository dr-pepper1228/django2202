# pip    : pypi.org 에서 코드를 본인의 컴퓨터에 설치하는 것!
# import : 다른 파일의 클래스, 함수, 변수를 가져다 사용함 


# googletrans
import googletrans
from googletrans import Translator
 
print(googletrans.LANGUAGES) 
# 이거 주석 해제하고 실행하면 나라별 코드 나옴(딕셔너리 형식)
 
text1 = "Hello welcome to my website!"
translator = Translator() # 트렌스레이터 클래스에 있는걸 전부 부여해준다
print(translator.detect(text1))
trans1 = translator.translate(text1, src='en', dest='ko')
print("English to Japanese: ", trans1.text)
