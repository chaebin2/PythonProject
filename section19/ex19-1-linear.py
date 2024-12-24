'''
파일명: ex19-1-linear.py

자료구조
    데이터를 저장하고 조직화하는 방법론

선형리스트(linearlist)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것
'''

class LinearList():
    def __init__(self):
        self.linear = [] # 빈 리스트 생성

    # 리스트에 데이터 추가 (사실 파이썬은 그냥 append 하면 되지만...)
    def add_data(self, data):
        linear = self.linear
        linear.append(None)
        lLen = len(linear)
        linear[lLen - 1] = data

    def print_list(self):
        linear = self.linear
        for item in linear:
            print(item)

# 실행 코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.print_list()
