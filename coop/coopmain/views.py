from django.shortcuts import render


# index 함수의 매개변수 request : 장고에 의해 자동으로 전달되는 HTTP 요청 객체
#                                사용자가 전달한 데이터를 확일할 때 사용
def index(request): 

    return render(request, 'coopmain/mainpage.html')
