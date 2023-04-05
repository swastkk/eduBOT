from django.urls import path
from account.views import home, register
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/newlogin.html',
         next_page='/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/account/login'), name='logout'),
    path('', home, name='home'),
    path('register/', register, name='register'),
]
