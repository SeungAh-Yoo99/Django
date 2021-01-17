# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAzMjFfMTAz%2FMDAxNTg0NzY0ODM1ODk5.gx6e3nGwsp_Gas0_4Bu4LQPMj0uQw80BuZ46SUSOwN4g.6tmZ74la0Wrgf-Dm6US_wRvObmlQ7h2CWseG2bwIjhcg.JPEG.du_90%2FIMG_3095.JPG&type=sc960_832'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = 'C:/Users/ysa84/OneDrive/문서/GitHub/Django/08. 크롤링 기초/test1.jpg'
save_path2 = 'C:/Users/ysa84/OneDrive/문서/GitHub/Django/08. 크롤링 기초/index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succeed')