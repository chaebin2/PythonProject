'''
파일명: ex13-1-makefile.py

파일 입출력(i/o - input/output)
    입력(input)

'''

file = open('myfile.txt', 'wt')
print('myfile.txt 파일이 생성되었습니다.')
file.close()

# with 문 - 자동으로 close()를 해준다.
with open('myfile2.txt', 'wt') as file:
    print('myfile2.txt 파일이 생성되었습니다.')
    