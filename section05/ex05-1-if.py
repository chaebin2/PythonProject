'''
파일명: ex05-1-if.py

    들여쓰기를 사용하여 코드의 범위 정의
'''
a = 100
b= 200

'''
tmp = a
a = b
b = tmp
'''

if b > a:
    print('b는 a보다 크다.')
else:
    print('바보')

#if ~ elif ~ else

age = 15
if age >= 18:
    print('성인 입니다.')
elif age >= 13:
    print('청소년 입니다.')
elif age >= 8:
    print('어린이 입니다.')
else:
    print('영유아 입니다.')