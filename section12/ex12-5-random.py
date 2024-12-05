'''
파일명: ex12-5-random.py
'''

import random

# 두 인자 사이 난수
print(random.randint(1, 10)) # 1~10 난수 생성
print()

# randrange - range 범위에 난수 생성
print(random.randrange(10)) # 0~9
print(random.randrange(1, 10)) # 1~9
print(random.randrange(1, 10, 2)) # 1~9 홀수만
print()

# 0이상 1미만 난수 생성
print(random.random())

if random.random() < 0.5:
    print('당첨!')
else:
    print('꽝!')
print()

# choice 함수 -리스트에서 랜덤
season = ['spirng', 'summer', 'fall', 'winter']
print(random.choices(season))
print()

#shuffle()함수 - 임의로 섞는 함수
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
