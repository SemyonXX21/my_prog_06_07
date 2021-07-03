from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('user', user_page, name='user'),

]
