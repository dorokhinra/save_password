from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  PassHome.as_view(), name='home'),
    path('login/', login, name='login'),
    path('setting_pass/', setting_pass_ya_disk, name='setting_pass'),
    path('pass_reestr/<str:parent_id>', PassReestr.as_view(), name='pass_reestr'),
    path('edit_reestr/', EditReestr.as_view(), name='edit_reestr'),
    path('encryption/', encryption, name='encryption'),
    path('delete_category/<str:pk>', DeleteCategory.as_view(), name='delete_cat'),
    path('delete_element/<str:pk>/delete', DeleteElement.as_view(), name='delete_element'),
    path('decrypt_elem/<str:pk>/', DecryptElem.as_view(), name='decrypt')
]