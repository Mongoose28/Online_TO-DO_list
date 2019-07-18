from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('delete/<list_id>',views.delete,name="delete"),
    path('cross_off/<list_id>',views.cross_off,name="cross_off"),
    path('uncross/<list_id>',views.uncross,name="uncross"),
    path('edit/<list_id>',views.edit,name="edit"),
    path('reg',views.register,name="reg"),
    path('login',views.login,name="login"),




]
