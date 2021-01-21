# Section04-3
# Requests
# requests 사용 스크랩핑(3) - Rest API

# Rest API : GET,  POST, DELETE, PUT:UPDATE, REPLACE(FRTCH : UPDATE, MODIFY)
# 중요 : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET : www.movies.com/movies :영화를 전부 조회
# GET : www.movies.com/movies/:id: : 아이디가 id인 영화를 전부 조회
# POST : www.movies.com/movies/ :영화를 생성
# PUT : www.movies.com/movies/ :영화를 수정
# DELETE : www.movies.com/movies/ :영화를 삭제

import requests

# 세션 활성화
s = requests.Session()

# 예제1
r = s.get('https://api.github.com/events')

# 수신상태 체크
r.raise_for_status()

# 출력
print(r.text)

# 에제2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies')