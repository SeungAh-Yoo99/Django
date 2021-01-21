# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))  # status와 같은 결과값 출력
print('read : {}'.format(mem.read(100).decode('utf-8'))) # 100byte를 읽어온다
print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))