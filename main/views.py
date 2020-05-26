from django.shortcuts import render,redirect,get_object_or_404
from .models import Board
from django.utils import timezone

# Create your views here.

def home(request) :
    return render(request, 'home.html')

def new(request) :
    return render(request, 'new.html')

def create(request) :
    new_board = Board()
    new_board.title = request.POST.get('title')
    new_board.pub_date = timezone.datetime.now()
    new_board.body= request.POST['body']
    # new_board.meeting_time = request.POST['meeting_time']
    new_board.number = request.POST['number']
    new_board.location = request.POST['location']
    new_board.save()
    return redirect('board')

def board(request) :

    boards= Board.objects.all()

    return render(request, 'board.html',{'boards':boards})

def detail(request,board_id) :
    board = get_object_or_404(Board, pk = board_id) 
    return render(request, 'detail.html',{'board':board})