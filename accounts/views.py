from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

# Create your views here.

User = get_user_model()

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,
                            password=password)
        if user is None:
            context['error'] = 'this user is not exists'
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html')


def register_view(request):
    return render(request, 'accounts/register.html')