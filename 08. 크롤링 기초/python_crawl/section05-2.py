# Section05-2
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().Chrome)]
# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구)
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# 검색어
quote = rep.quote_plus('호랑이')
# URL 완성
url = base + quote

# 요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "./imagedown/"

# 폴더 생성 예외 처리(문제 발생 시 프로그램 종료)
try:
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러 내용
    print("folder creation failed.")
    print("folder name : {}".format(e.filename))

    # 런타입 에러
    raise RuntimeError("System Exit!")
else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("folder is created!")


# bs4 초기화
soup = BeautifulSoup(res, "html.parser")
# print(soup.prettify())

# select 사용
img_list = soup.select("div.photo_tile._grid > div.tile_item._item > div.photo_bx.api_ani_send._photoBox > div.thumb > a.link_thumb._imageBox._infoBox > img")
# 이 부분에서 막힌다.
# div.photo_tile._grid > div.tile_item._item로 넘어가는 부분이 읽어온 html에 없었다.
# 찾아보니 이 부분은  동적으로 생성되는 부분이라 읽어오지 못하는 것 같다.
# 이 부분은 페이지가 로딩된 후, 나중에 자바스크립트를 이용해 동적으로 추가하는 것 같아서 selenium을 이용해야 한다고 한다.
# 강의 시점과 실습 시점 사이에 뭔가 바뀐 모양이다.
# selunium은 다음 챕터에서 배우므로 그냥 넘어가서 뒷부분 따라해보기만 하고 결과 확인은 못할 것 같다.

# print(img_list)

for i, img in enumerate(img_list, 1):
    # 속성 확인
    # print(img['data-source'], i)

    # 저장 파일명 및 경로
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    # 파일명 확인
    # print(fullFileName)

    # 다운로드 요청(URL, 다운로드 경로)
    req.urlretrieve(img['data-source'], fullFileName)

# 다운로드 완료 시 출력
print("download succeed!")