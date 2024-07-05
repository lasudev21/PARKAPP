from django.urls import path

from .views import index, login, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
]