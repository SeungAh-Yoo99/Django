# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time ther were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id="link3">title</a>
        </p>
        <p class="story">
            story....
        </p>
    </body>
</html>
"""
# 예제1(BeautifulSoup 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser') # html 파일을 가져오지 않았다면, 첫번째 인자로 request.get(주소)를 해준다.

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify)

# bs4의 함수 확인
print(dir(soup))

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p # 가장 첫번째 요소만 나온다.
print('p1', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling # .next_sibling 한 번 호출 시, </p> 뒤에 가고 한 번 더 호출하면 다음 p 태그로 갈 수 있다.
print('p2', p2)

# 텍스트 출력1
print('h1 >>', h1.string)

# 텍스트 출력2
print('p1 >>', p1.string) # p 태그 안의 b 태그는 무시하고 string만 출력함.

# 다음 엘리먼트 확인
print(list(p2.next_element)) # p2 안의 텍스트 부분이 출력된다.
