from django.shortcuts import render
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_write(request):
    form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # '-'는 역순으로 가져온다는 뜻.(여기서는 최신순으로 가져온다는 뜻.)
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})
