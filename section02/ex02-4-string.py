'''
 파일명: ex02-4-string.py

 문자열(string, str)
    - 문자들의 순서가 있는 나열
    - 작은따옴표(') 또는 큰따옴표(")로 표현
    - 문자열은 변경불가능(immutable)
'''

# 1. 문자열 생성 방법
str1 = 'hello python' # 작은 따옴표
str2 = "hello python" # 큰 따옴표
str3 = '''hello
python
''' # 여러줄 문자열(이것도 ', " 다 됨)

print(str1)
print(str2)
print(str3)

# 2. 문자열 인덱싱
'''
        h   e   l   l   o
index   0   1   2   3   4
역순번호 -5  -4  -3  -2  -1

'''
str1 = 'hello'
print('첫번째 문자:', str1[0])
print('첫번째 문자:', str1[4])
print('첫번째 문자:', str1[-1])

# 3. 문자열 슬라이싱
str = 'python programming'
print('처음부터 5번째글자 전까지:', str[0:4]) #[a1, a2] 이면 a1부터 (a2-a1)개 뽑는다 생각 a2전까지 뽑는느낌임
print('처음부터 6번째글자 전까지:', str[0:6])
print('두번째부터 4번째 글자 전까지:', str[1:3])
print('5번째부터:', str[4:])
print('마지막 5글자:', str[-5:])

# 4. 주요 문자열 메소드(함수)
str = ' p y t h o n  '
print('원본:', str)
print('공백제거:', str.strip()) #글자 사이사이 공백은 제거 x 앞,뒤 공백만 제거
print('모두 대문자:', str.upper())
print('모두 소문자:', str.lower())
print('문자 교체:', str.replace('p', 'j'))
print('문자 사이 공백 제거:', str.replace(' ', ''))
