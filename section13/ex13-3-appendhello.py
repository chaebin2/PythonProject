'''
파일명: ex13-3-appendhello.py
a(append mode): 추가 모드

'''

with open('hello.txt', 'at', encoding='utf-8') as file:
    file.write('hello\n')
    file.write('nice to meet you')

print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')