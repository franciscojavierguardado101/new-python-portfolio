from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse_lazy

# Create your views here.
def register(response):
      if response.method == 'POST':
            form = RegisterForm(response.POST)
            if form.is_valid():
                  form.save()
            return redirect("login")
      else:
            form = RegisterForm()
      return render(response, "registration/register.html", {'form': form})


#login code
def login(request):
      if request.user.is_authenticated:
            return redirect('blog:home')
      if request.method == 'POST':
            username = str(request.POST['username'])
            password = str(request.POST['password'])
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                  auth.login(request, user)
                  return redirect('blog:home')
            else:
                  return redirect('login')
      else:
            return render(request,'registration/login.html')


@login_required
def logout(request):
      auth.logout(request)
      return redirect('login')