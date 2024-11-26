'''
파일명: ex04-5-bitwise.py

비트 연산자
    이진수의 비트 단위 연산자
    & (and): 두 비트 모두 1일때 1
    | (or): 하나라도 1이면 1
    ^ (xor): 두 비트가 다르면 1
    ~ (not): 비트 반전
    <<(left shift) : n칸 왼쪽 비트 이동
    >>(right shift): n칸 오른쪽 비트 이동
'''
a = 6 # 0110
b = 5 # 0101

print(f'a & b: {a & b}')
print(f'a | b: {a | b}')
print(f'a ^ b: {a ^ b}')
print(f'~a: {~a}')

print(f'a << 1: {a << 1}')
print(f'a >> 1: {a >> 1}')