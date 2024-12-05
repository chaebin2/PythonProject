'''
파일명: ex14-4-csvreader.py

'''

import csv

with open('차량관리.csv', 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        print(line)
        print(line[1])