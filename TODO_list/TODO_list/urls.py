from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home',views.home, name="home"),
    path('delete/<list_id>',views.delete,name="delete"),
    path('cross_off/<list_id>',views.cross_off,name="cross_off"),
    path('uncross/<list_id>',views.uncross,name="uncross"),
    path('edit/<list_id>',views.edit,name="edit"),
    path('reg/',views.registers,name="reg"),
    path('',views.logins,name="login"),




]
