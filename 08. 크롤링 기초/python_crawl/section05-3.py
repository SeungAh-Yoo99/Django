# Section05-3
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(3) - 로그인 처리

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Login 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': 'ysa8497',
    'isSaveId': 'true',
    'password': 'dyoosungaa0704**'
}

# Headers 정보
headers = {
    "User-Agent": UserAgent().chrome,
    "Referer": 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F'
}

with req.session() as s:
    # Request(로그인 시도)
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    # 로그인 시도 실패 시 예외
    if res.status_code != 200:
        raise Exception("Login failed!")

    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))

    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

    # Euc-kr(한글이 ㄲ개질 경우)
    # res.encoding = 'enc-kr'

    # 페이지 이동 후 수신 데이터 확인
    print(res.text)