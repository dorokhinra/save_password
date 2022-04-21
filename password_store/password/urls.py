from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  PassHome.as_view(), name='home'),
    path('login/', login, name='login'),
    path('setting_pass/', setting_pass, name='setting_pass'),
    path('pass_reestr/', pass_reestr, name='pass_reestr'),
    path('edit_reestr/', edit_reestr, name='edit_reestr')
]