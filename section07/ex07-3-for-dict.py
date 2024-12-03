'''
파일명: ex07-3-for-dict.py
'''
# key:value 꼴로 이루어진 dict 생성
eng_dict = {
    'sun': '태양',
    'moon': '달',
    'star': '별',
    'space': '우주'
}

for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict[word]}')
    # = print(f'{word}의 뜻: {eng_dict.get(word)}')

eng_dict_keys = eng_dict.keys()
for k in eng_dict_keys:
    print(f'eng_dict의 key: {k}')

eng_dict_values = eng_dict.values()
print(eng_dict_values)
for v in eng_dict_values:
    print(f'eng_dict의 벨류: {v}')