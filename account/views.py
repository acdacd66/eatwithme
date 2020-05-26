from .models import User
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from main.models import Board
# Create your views here.

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], 
                    password=request.POST['password1'],
                    code = request.POST['code'],
                    department = request.POST['department'])
                    
    
                auth.login(request, user)
               

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:   #유저가 none 이 아니면은 로그인 조져라  그다음에 홈창으로 가주는거임
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def mypage(request):
    mypage_info = User.objects.get(username=request.user.username)
    my_post=Board.objects.filter(writer=request.user.username)
    return render(request,'mypage.html',{"my_post": my_post}) 

def edit(request, user_id):
    edit_user = get_object_or_404(User, pk = user_id)
    return render(request, "edit.html", {"user": edit_user})

def update(request, user_id):
    update_user = get_object_or_404(User, pk = user_id)
    update_user.code = request.POST['code']
    update_user.department = request.POST['department']
    update_user.save()
    return redirect('mypage')
