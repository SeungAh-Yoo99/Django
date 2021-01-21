# Section04-2
# Requests
# requests 사용 스크랩핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100', stream=True) # stream 옵션은 데이터를 직렬화해서 가져온다.

# 수신 확인
print(r.text)

# Encoding 확인
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))