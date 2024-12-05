'''
파일명: ex13-4-readhello.py
open 함수 모드
    r(read mode): 읽기 전용 모드/ 파일이 없으면 에러
'''

with open('hello.txt', 'rt', encoding='utf-8') as file:
    #str = file.read() # 전체 읽기
'''
    while True:
        str = file.readline() # 한줄씩 읽기
        if not str: # 파일 끝에 도달하면 종료
            break
        print(str, end='')
'''