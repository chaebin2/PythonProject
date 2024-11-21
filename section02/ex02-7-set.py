'''
파일명: ex02-7-set.py


'''

# 1. 세트 생성과 기본 기능
pokemon_type = {'불꽃', '물', '전기', '풀'}
print('포켓몬 속성:', pokemon_type)

# 2. 세트 수정
fire_type = {'파이리', '마그마', '브케인'}

# 4. 세트 제거 메서드
water_type = {'꼬부기', '잉어킹', '라프라스'}
water_type.remove('잉어킹') # 없는 값을 리무브하면 에러남
print('remove 후:', water_type)

water_type.discard('없는포켓몬')
print('dis사용:', water_type)

water_type.pop() # 임의 제거
print('pop후:', water_type)

new_type = {'메가이브이', '뮤'}
print(new_type)
new_type.clear() #전체제거
print('clear후:', new_type)