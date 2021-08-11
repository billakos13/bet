from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Congratulations {username}, your account has been created!Please log in.")
            form.save()
            return redirect('login')
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {})


