'''
파일명: ex06-2-while.py
'''

my_list = []
n = int(input('정수를 입력하세요(종료는 0 입니다.) >>>'))
while n != 0:
    my_list.append(n) #리스트 맨 마지막에 x를 추가하는 함수
    n = int(input('정수를 입력하세요(종료는 0 입니다.) >>>'))


print(my_list)