from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  PassHome.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('setting_pass/syncronization/',  sync_to_async(login_required(async_to_sync(SyncDisc.as_view()), login_url='login')),
         name='setting_pass'),
    path('setting_pass/syncronization/<slug:ts>/download/', SyncDisc.as_view(), name='download'),
    path('pass_reestr/<str:parent_id>', login_required(PassReestr.as_view(), login_url='login'), name='pass_reestr'),
    path('edit_reestr/', login_required(EditReestr.as_view(), login_url='login'), name='edit_reestr'),
    path('setting_pass/encryption/', login_required(EncryptView.as_view(), login_url='login'), name='encryption'),
    path('delete_category/<str:pk>', DeleteCategory.as_view(), name='delete_cat'),
    path('delete_element/<str:pk>/delete', DeleteElement.as_view(), name='delete_element'),
    path('decrypt_elem/<str:pk>/', DecryptElem.as_view(), name='decrypt'),
    path('update_elem/<str:pk>/', UpdateElem.as_view(), name='update_elem'),
    path('logout/', logout_user, name='logout'),
    path('upload_key/', DownloadUserKey.as_view(), name='upload_user_key_file'),
    path('delete_user_key/<str:pk>/', DeleteUserKey.as_view(), name='delete_user_key'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('accept_register/<str:reg_id>/', AcceptRegister.as_view(), name='mail_view')
]