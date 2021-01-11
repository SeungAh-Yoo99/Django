from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404  # 내용을 찾을 수 없을 때, 대신 내보낼 수 있는 페이지
from fcuser.models import Fcuser
from tag.models import Tag
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue
                # name=tag에 일치하는 조건의 tag가 있으면 가져오고, 없으면 생성 후 가져온다.
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # '-'는 역순으로 가져온다는 뜻.(여기서는 최신순으로 가져온다는 뜻.)
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))  # p번째 페이지, 지정이 안되어 있으면 1 페이지
    paginator = Paginator(all_boards, 2)  # 한 페이지 당 2개 씩 보여주는 것으로 설정

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})
