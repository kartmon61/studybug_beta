from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# 로그인 함수
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'main.html')
        else:
            return render(request,'login.html',{'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 회원가입 함수
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['email'],password=request.POST['password1'])
            auth.login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return render(request,'signup2.html')
    return render(request,'login.html')

#로그아웃 함수
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request,'login.html')

# 로딩 화면     
def loading(request):
    return render(request,'loading.html')

# 관심사 고르기   
def signup2(request):
    return render(request,'signup2.html')

