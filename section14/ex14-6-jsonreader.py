'''
파일명: ex14-6-jsonreader.py

'''
import json
with open('dictlist.json', 'r', encoding='utf-8')as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

    for dic in dict_list:
        print(f'이름: {dic['name']}')
        print(f'나이: {dic['age']}')
        print(f'키: {dic['spec'][0]}')
        print(f'몸무게: {dic['spec'][1]}')