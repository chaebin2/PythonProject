'''
파일명: ex12-7-external.py

라이브러리 - 패키지 집합

패키지
    모듈의 상위 개념
    모듈의 집합을 의미

pip - 패키지 관리 도구
    pypi(python package index)에서 패키지를 다운로드 한다.
    수많은 오픈소스가 저장되어 있는 중앙 저장소

패키지 설치 명령어
    pip install 패키지명

패키지 삭제 명령어
    pip uninstall 패키지명

'''
from sys import base_prefix

# 행렬 연산 관련 package
import numpy as np

print(np.sum([1, 2, 3, 4, 5]))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)

d = a - b
print(d)