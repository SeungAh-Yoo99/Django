# Section06-3
# Selenium
# Selenium 사용 실습(3) - 실습 프로젝트(2)

# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless") # 실행 했을 때 브라우저가 실행되지 않는다.

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
# browser = webdriver.Chrome('D:/webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
browser = webdriver.Chrome('D:/webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭1 (2보다 1의 방법이 더 보편화 되어 있다.)
# Explicitly wait
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
# 3초간 기다리되, 버튼이 나타나면 클릭을 한다.

# 제조사별 더 보기 클릭2
# Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()
# 2초간 계속 기다린다.

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents : {}'.format(browser.page_source))

# 2초간 대기
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 5

while cur_page <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스코드 정리
    # print(soup.prettify)

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer ')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('****** Current Page : {} ******'.format(cur_page))
    print()

    # 필요 정보 추출
    for v in pro_list:
        # 임시 출력
        #print(v)

        # 상품명, 이미지, 가격
        s = v.select('div.prod_main_info > div.prod_info > p > a[name="productName"]')
        if s:
            print(s[0].text.strip())
            print(v.select('div.prod_main_info > div.thumb_image > a.thumb_link > img')[0]['src']) # 이미지 불러오는 것은 막힌 것 같다.
            print(v.select('div.prod_main_info > div.prod_pricelist > ul > li > p.price_sect > a > strong')[0].text.strip())

            # 이 부분에서 엑셀 저장(파일, DB 등)
            # CODE
            # CODE

        print()
    print()

    # 페이지 별 스크린 샷 저장
    browser.save_screenshot('./target_page{}.png'.format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Craling Succed.')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()
    # 처음에 3초로 했더니 에러가 발생했다.
    # 시간을 늘려 4초로 했더니 잘 돌아간다.
    # 이 부분에서 중간에 에러가 난다면 시간을 늘려보자.

    # BeautifulSoup 인스턴스 삭제
    del soup
    
    # 3초간 대기
    time.sleep(3)

# 브라우저 종료
browser.close()