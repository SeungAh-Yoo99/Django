# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)

import requests
import lxml.html

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com") # Get, Post

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        # url 출력
        print (url)

def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect(''):
        # 링크

# 스크랩핑 시작
if __name__ == "__main__":
    main()