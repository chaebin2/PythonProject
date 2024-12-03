'''
파일명: ex07-4-for-dict2.py

이름	    국어	영어	수학
John	90	85	95
Emily	92	88	96
Michael	98	90	92
Jessica	88	82	78

json
(Java Script Objectr Notation)
'''

students = [
    {'이름': 'John', '국어': 90, '영어': 85, '수학': 95},
    {'이름': 'Emily', '국어': 92, '영어': 88, '수학': 96},
    {'이름': 'Michael', '국어': 98, '영어': 90, '수학': 92},
    {'이름': 'Jessica', '국어': 88, '영어': 82, '수학': 78}
    ]

for student in students:
    ''' (리스트기준)for문으로 student에 데이터가 담김
    0: student = {'이름': 'john', '국어': 90, '영어': 85, '수학': 95}
    1: student = {'이름': 'Emily', '국어': 92, '영어': 88, '수학': 96}
    2: student = {'이름': 'Michael', '국어': 98, '영어': 90, '수학': 92}
    3: student = {'이름': 'Jessica', '국어': 88, '영어': 82, '수학': 78}
    
    '''
    print(f'{student['이름']}', end=' ')
    print(f'{student['국어']}', end=' ')
    print(f'{student['영어']}', end=' ')
    print(f'{student['수학']}', end=' ')
    print()

mike = students[2] # michael 에 대한 정보
for k, v in mike.items(): # key, value 둘다 가져오는 또 다른 방법.
    print(f'{k}: {v}')