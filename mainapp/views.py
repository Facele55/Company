from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.EmailBackEnd import EmailBackEnd
from mainapp.forms import CustomUserCreationForm
from mainapp.models import CustomUser


def home(request):

    return render(request, 'mainapp/index.html')


def portfolio(request):
    return render(request, 'mainapp/portfolio.html')


def about_us(request):
    return render(request, 'mainapp/about_us.html')


def login_page(request):
    return render(request, 'login/signin.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.create_user(username=username, password=raw_password, email=email)
            user.save()
            login(request, user)
            return redirect('user_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/sign_up.html', {'form': form})


def do_login(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                 #return HttpResponse("Staff Login")
                return redirect('staff_home')

            elif user_type == '3':
                # return HttpResponse("User Login")
                return redirect('user_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            # return HttpResponseRedirect("/")
            return redirect('login')


def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
