from django.shortcuts import render

from mainapp.models import CustomUser


def user_home(request):
    return render(request, 'user_template/user_home.html')


def user_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'user_template/user_profile.html', context)
