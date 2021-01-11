from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'  # 정상적으로 모든 정보가 입력 됐을 때 이동할 주소
