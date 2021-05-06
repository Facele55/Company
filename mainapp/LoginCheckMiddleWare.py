from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse, include


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #  Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "mainapp.AdminView":
                    pass
                elif modulename == "mainapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")
            
            elif user.user_type == "2":
                if modulename == "mainapp.StaffView":
                    pass
                elif modulename == "mainapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("staff_home")
            
            elif user.user_type == "3":
                if modulename == "mainapp.UserViews":
                    pass
                elif modulename == "mainapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("user_home")

            else:
                return redirect("login")

        else:
            pass
