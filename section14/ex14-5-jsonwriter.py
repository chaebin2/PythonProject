'''
파일명: ex14-5-jsonwriter.py

json(java script object notation)
    데이터를 키와 값의 쌍을 중괄호로 묶어 표현하는 형싱
    - 딕셔너리와 비슷하다
    - 구조 {k:v}
'''

import json

dict_list = [
    {
        'name':'james',
        'age':20,
        'spec':[175.5, 70.5]
    },
    {
        'name':'alice',
        'age':21,
        'spec':[168.5, 60.5]
    }
]

json_string = json.dumps(dict_list, indent=4)

with open('dictlist.json', 'w') as file:
    file.write(json_string)

print('dictlist.json 파일이 생성되었습니다.')