'''
파일명: EX08-4-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''

total = 0
for n in range(1, 101):
    if n % 3 == 0: # %:나머지
        continue
    total += n
    print(f'n: {n}, total: {total}')