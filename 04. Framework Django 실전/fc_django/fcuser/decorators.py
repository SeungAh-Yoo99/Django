from django.shortcuts import redirect
from .models import Fcuser


def login_required(function):
    def wrap(request, *args, **kwargs):  # 래핑한 함수와 기존 함수의 인자값을 맞춰줘야 한다.
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap
