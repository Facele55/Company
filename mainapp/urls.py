from django.urls import path
from . import views, AdminView, UserViews, StaffView


urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about_us, name="about_us"),
    path('login/', views.login_page, name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('do_login/', views.do_login, name="do_login"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),

    path('admin_home/', AdminView.admin_home, name="admin_home"),
    path('staff_home/', StaffView.staff_home, name="staff_home"),
    path('user_home/', UserViews.user_home, name="user_home"),
    path('user_profile/', UserViews.user_profile, name="user_profile"),
    path('sign_up/', views.signup, name="sign_up")

]
