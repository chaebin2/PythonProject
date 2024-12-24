'''
파일명: ex20-3-O(2^n).py

O(2^n)
    지수 시간 복잡도, 피보나치 수열처럼 재귀적 알고리즘
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(15))
# 복잡도가 쉽지 않아서 큰 숫자를 넣으면 하루종일 걸린다...