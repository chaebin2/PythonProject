'''
파일명: ex03-2-print.py

print() 함수
    - sep: 값 사이 구분자(기본: 공백)
    - end: 출력 끝 문자(기본: \n)
    - file: 출력 대상(기본: sys.stdout)


'''

# 1. 기본 출력
pokemon = '피카츄'
level = 25
print('포켓몬:', pokemon, '레벨:', level)

# 2. sep 매개변수
stats = ['피카츄', '전기', 35, 55]
# * 언패킹(unpacking) 피카츄 전기 35 55
print(stats)
print(*stats)
print(*stats, sep=',') # 싐표로 구분

# 3. end 매개변수
print('피카츄', end='>')
print('라이츄', end='>')
print('파이리')
print('테스트1')
print('테스트2')

# 4. 파일출력
with open('pokemon.txt', 'w', encoding= 'utf-8') as file: # w:쓰기 권한
    print('name: 피카츄', file=file)
    print('type: 전기', file=file)

