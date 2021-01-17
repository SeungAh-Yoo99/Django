# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["C:/Users/ysa84/OneDrive/문서/GitHub/Django/08. 크롤링 기초/test1.jpg", "C:/Users/ysa84/OneDrive/문서/GitHub/Django/08. 크롤링 기초/index.html"]

# 다운로드 리소스 url
target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDEyMzFfNDcg%2FMDAxNjA5NDE1MTM5NzM3.UNe-BZdnaFbotwaN3V2ELh4BlFh-Du67Q7AUxTWx7Agg.sImQw27dmuq7D1YBzBaVDz-tHV5bWQUk6MSQYbmEo-Mg.PNG.kimmiso3337%2F%25BB%25E7%25C0%25DA_12.png&type=a340", "http://google.com"]

for i, url in enumerate(target_url):
    #예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("--------------------------------------------------------------------------------------------------")

        # 상태 정보 중간 출력
        print('Headeer Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print("--------------------------------------------------------------------------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URLError Reason : ", e.reason)

    # 성공
    else:
        print()
        print("Download Succeed.")