'''
파일명: ex18-1-requests.py

URL(Uniform Resource Locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을 수 있는 주소

프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 표준화된
    규칙, 절차, 통신 프로세스를 의미

    ex) http/https - 웹 서버 프로토콜
        ftp - 파일 서버 프로토콜
        mailto - 메일 서버 프로토콜
        telent - 원격지 프로토콜

호스트(host)
    리소스가 위치한 서버의 이름
    EX) n.news.naver.com

포트(Port)
    서버에서 사용하는 방번호
    http - 80, https - 443

경로(Path)
    웹 서버에서 자원에 대한 경로
    ex) /article/003/0012954121

쿼리(query) - 추가로 서버에 보내는 데이터(parameter)
    ex) ?ntype=RANKING
'''

import requests
# ?ntype =RANKING
url = 'https://n.news.naver.com/article/003/0012954121'
params = {
    'ntype':'RANKING'
}

response = requests.get(url, params=params)
print(response.text)