from django.shortcuts import render, redirect
from .forms import LoginForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #profile_id = request.session.get('ref_profile')
        if form.is_valid():
            new_user = form.save(commit=False)
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()

            # messages.success(request, f'Congratulations {username}, your account has been created')
            messages.success(
                request, 'Congratulations {}, your account has been created .'.format(new_user))
            # return redirect('register:login')

    return render(request, 'accounts/register.html', {
        'title': 'register',
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        try:
            user = authenticate(request, username=User.objects.get(
                email=username), password=password)

        except:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(
                request, f'Welcome {username} You are logged in successfully')
            # return redirect('products:homepage')

        else:
            messages.warning(request, ' username or password is incorrect')

    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {
        'title': 'Login',
        'form': form
    })


# def login(request):
#     return render(request, "accounts/login.html")


def forgot_password(request):
    return render(request, "accounts/forgot-password.html")
