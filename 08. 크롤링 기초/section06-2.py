# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)

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

