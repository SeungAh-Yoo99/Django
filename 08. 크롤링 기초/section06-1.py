# Section06-1
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트

# slsnium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
browser = webdriver.Chrome('D:/webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 속성 확인
print(dir(browser))

# 브라우저 사이즈
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 펭이지 이동
browser.get('https://www.daum.net')