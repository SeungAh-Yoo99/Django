from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):  # 현재 로그인 되어 있는 상태인지(세션에 정보가 있는지) 확인
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # 유효성 검사 후 유효하지 않으면 form에 에러 정보가 저장된다.
            # session
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):  # url에 연결 시 요청 정보가  'request'라는 변수를 통해서 들어온다.
    if request.method == 'GET':  # 주소 값으로 서버 요청을 보낼 때
        return render(request, 'register.html')
    elif request.method == 'POST':  # 등록 버튼으로 서버 요청을 보낼 때
        # Post는 딕셔너리 형태, 값을 지정하지 않으면 None이 저장되게 한다.
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}  # 에러 메세지를 담을 변수

        if not (username and password and re_password and username):  # 네 값 중 하나라도 입력하지 않으면 에러 처리
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            fcuser = Fcuser(  # 입력 받은 값으로 객체 생성
                username=username,
                useremail=useremail,
                password=make_password(password)  # 암호화 해서 password를 저장
            )

            fcuser.save()
            # 객체 db에 저장

        # 다시 register.html를 return하기 때문에 원래 페이지가 반환됨.
        return render(request, 'register.html', res_data)
