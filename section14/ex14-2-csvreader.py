'''
파일명: ex14-2-csvreader.py

csv(comma-separated values)
    필드를 쉼표로 구분한 텍스트 데이터 파일
'''
import csv

member_list = []
with open('회원명단.csv', 'rt', encoding='utf-8') as file:
    file.readline()
    while True:
        line = file.readlines()
        if not line:
            break

        member = line.split(',')
        member_list.append(member)

print(member_list)