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
    'password': 'dyoosungaa0704**'
}