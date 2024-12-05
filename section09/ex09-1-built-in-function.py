'''
파일명: ex09-1-built-in-function.py

내장함수
    파이썬에서 제공해주는 별도의 import 없이
    사용할 수 있는 함수
'''

# 예제1: 리스트와 관련된 내장 함수들
number = [1, -5, 2, 3, -8, 3, 9, -3, 4, 7, -1]
print('1.합계:', sum(number))
print('2. 최대값:', max(number))
print('3. 최소값:', min(number))
print('4. 정렬된 리스트:', sorted(number))
print('5. 절대값 맵핑:', list(map(abs, number)))
print('6. 리스트 길이:', len(number))

# 예제2: 문자열과 관련된 함수들
text = "python programming 123"
words = ['apple', 'banana', 'cherry', 'date']
str_alpha = 'abc'
str_numeric = '123'