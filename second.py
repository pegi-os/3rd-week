import requests
import random

url = "http://docker-service1-1:5000"  # 1번째 서비스의 주소

number = 2 # 1~20 범위의 랜덤한 숫자 생성

data = {
    "number": number  # 전송할 데이터
}

response = requests.post(url, data=data)
print(response.text)  # 서버로부터 받은 응답 출력
