from django.conf.urls import url
from . import views
 
app_name = 'games'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loginpage/', views.loginpage, name='loginpage'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^myAccount/', views.myAccount, name='myAccount'),
    url(r'^reward/', views.reward, name='reward'),
    url(r'^purchased/', views.purchased, name='purchased'),
]


