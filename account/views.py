from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
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
                    request.POST['username'], password=request.POST['password1'])
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



