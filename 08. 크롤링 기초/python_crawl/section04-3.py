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


# 예제1(GET)
r = s.get('https://api.github.com/events')

# 수신상태 체크
r.raise_for_status()

# 출력
# print(r.text)


# 에제2(GET)
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies')

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
# print(r.text)


# 예제3(GET)
r = s.get('https://github.com', timeout=5)

# 출력
# print(r.text)


# 예제4(POST)
r = s.post('http://httpbin.org/post', data={'id':'test1', 'pw':'1111'}, cookies=jar)

# 출력
# print(r.text)
# print(r.headers)


#예제5(POST)
payload1 = {'id':'test1', 'pw': '1111'}
payload2 = (('id', 'test2'), ('pw', '2222'))

r1 = s.post('http://httpbin.org/post', data=payload1)
r2 = s.post('http://httpbin.org/post', data=payload2)

# 출력
# print(r1.text)
# print(r2.text)


# 예제6(PUT)
r = s.put('http://httpbin.org/put', data=payload1)

# 출력
# print(r.text)


# 예제7(DELETE)
r = s.delete('http://httpbin.org/delete', data={'id' : 1}) # id가 1인 data를 삭제하길 원함

# 출력
# print(r.text)


# 예제8(DELETE)
r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.ok)
print(r.text)

s.close()