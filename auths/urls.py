from django.urls import path
from auths import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('/index', views.index_page, name='index_page'),
]
