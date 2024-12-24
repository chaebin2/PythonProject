'''
파일명: ex19-0-recursive.py

재귀함수(recursive function)
    함수 내부에서 자기자신을 호출하는 함수
'''

def recursive_count_number(n):
    ''' 코드 돌아가는 순서
    recursive_count_number(5) << 안끝남
        n= 5
        print(5)
        recursive_count_number(4) << 안끝남
            n = 4
            print(4)
            recursive_count_number(3) << 안끝남
                n=3
                ...
                    n=0
                        if(n <=0):
                            return << 리턴하고 쭈루루룩 끝남

    '''
    if(n <=0):
        return
    print(n)
    recursive_count_number(n - 1)

# 실행코드
recursive_count_number(5)

print()

def count_number(n):
    while True:
        if(n<=0):
            break
        print(n)
        n -= 1

count_number(5)
