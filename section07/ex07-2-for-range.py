'''
파일명: ex07-2-for-range.py

for 문과 range() 함수

range()
    연속된 숫자를 만들어주는 함수
    예) range(1,10) => 1, 2, 3,..., 9
'''

dan = 2
#range (stop)
for n in range(10): # range(10): 0~9
    print(f'{dan} x {n} = {dan * n} ', end=" ")
print()
dan = 3
#range(start, stop)
for n in range(1,10): # range(1,10): 1~9
    print(f'{dan} x {n} = {dan * n}', end ='  ')
print()
dan = 4
#range(start, stop, step)
for n in range(1, 10, 2): # 1부터 2씩 증가 < 10
    print(f'{dan} x {n} = {dan * n}', end ='  ')
