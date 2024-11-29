from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('todo',views.to_do,name='to_do'),
    path('signup', views.signup, name='signup'), 
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout_view'),    
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),
]










 
