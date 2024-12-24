'''
파일명: ex20-1-O(1).py

빅오 표기법(big o notation)
    알고리즘의 시간 복잡도와 공간복잡도를 분석할 떄 사용되는 표기법
    빅오 표기법은 최악의 경우 성능 표현
'''
from wsgiref.util import request_uri


# O(1)
def return_first_value(arr):
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(arr[0])
    return arr[0]

# 실행코드
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(return_first_value(arr))

print()
#0(logN): 로그 시간 복잡도, 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘

def binary_search(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

#실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 11))

print()
# O(n): 입력 크기에 비례하여 시간이 걸리는 알고리즘

def linear_search(arr, x):
    size = len(arr)

    for i in range(size):
        if arr[i] == x:
            return i

    return -1

# 실행코드
arr = [1, 3, 4, 5, 9]
print(linear_search(arr, 5))

print()
# O(NlogN): 병합(머지)정렬 등의 알고리즘

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# 실행 코드
arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(merge_sort)
