from django.urls import path
from accounts.views import login_page, register, logout_page

urlpatterns = [
    path('', login_page , name='login_page'),
    path('logout/', logout_page , name='logout_page'),
    path('register/', register , name='register'),
]
