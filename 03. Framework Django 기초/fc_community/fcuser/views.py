from django.shortcuts import render

# Create your views here.


def register(request):  # url에 연결 시 요청 정보가  'request'라는 변수를 통해서 들어온다.
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        return render(request, 'register.html')
