'''
# 1. 문자열 카운팅
text = "사과 바나나 바나나 체리 사과 사과"
words = text.split()
print(words)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# 2. 짝수, 홀수 나누기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_odd = []
num_even = []
for num in numbers:
    if num %2 == 0:
        num_even.append(num)
    else:
        num_odd.append(num)

print(f'짝수:{num_even}')
print(f'홀수:{num_odd}')

# 3. 숫자 맞추기 게임
import random
attempts = 0
num = random.randint(1,100)
while True:
    num_input = int(input('숫자를 맞혀보세요:'))
    attempts += 1
    if num_input > num:
        print('더 작은 숫자를 입력하세요.')
    elif num_input < num:
        print('더 큰 숫자를 입력하세요.')
    else:
        print(f'정답입니다! 시도 횟수:{attempts}번')
        break
print()

# 4. 구구단

dan = 2
for n in range(1,10):
    print(f'{dan} x {n} = {dan * n}')

dan = 3
for n in range(1, 10):
    print(f'{dan} x {n} = {dan * n}')

dan = 4
for n in range(1,10):
    print(f'{dan} x {n} = {dan * n}')

dan = 2
while dan != 5:
    print(f'{dan}단')
    print('-'* 10)
    for n in range(1,10):
        print(f'{dan} x {n} = {dan * n}')
    print()
    dan += 1

# 5. 최대값과 최소값 찾기
numbers = [45, 2, 78, 34, 89, 21]
num_max = max(numbers)
num_min = min(numbers)
num_diff = num_max - num_min

print(f'최대값:{num_max}')
print(f'최소값:{num_min}')
print(f'최대값과 최소값의 차이:{num_diff}')

# 6. 문자열 뒤집기
str1 = 'hello'
print(f'정방향:{str1}')
print(f'역방향:{str1[::-1]}')
'''
# 7. 리스트의 중복 제거
numbers = [1, 2, 2, 3, 4, 4, 5]
num_list = []
for num in numbers:
    if num not in num_list:
        num_list.append(num)
print(num_list)

# 8. 피보나치 수열
fib_list = []
n = int(input('입력:'))
num1 = 0
num2 = 1
for f in range(n):
    fib_list.append(num1)
    num1, num2 = num2, num1 + num2

print(fib_list)