# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Header 스킵(첫번째 행은 생락하고 싶을 때 사용)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제3 (Dict변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f: #newline 옵션은 새로운 줄 바꿈을 처리해준다.
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(openpyxl, xlrd)
# 옵션 확인 : application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx')
# 옵션
# sheetname = '시트명' 또는 숫자(가져올 시트), header = 숫자(시작 행), skiprow = 숫자(스킵할 행)

# 상위 데이터 확인
print(xlsx.head())

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)