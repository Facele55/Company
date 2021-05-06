from django.shortcuts import render


def admin_home(request):
    return render(request, 'admin_template/admin_home.html')
