from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signin(request):
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장하기.
        username = request.POST['username']
        password = request.POST['password']
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect("home")
