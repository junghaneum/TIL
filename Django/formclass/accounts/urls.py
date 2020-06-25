from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), # User Create
    path('login/', views.login, name='login'), # Session Create
    path('logout/', views.logout, name='logout'), # Session Delete
    path('delete/', views.delete, name='delete'), # User Delete
    path('edit/', views.edit, name='edit'), # User Update
    path('password/', views.password, name='password'), # Password Update
    path('profile/', views.profile_detail, name='profile_detail'), # Profile Read
    path('profile/edit/', views.profile_edit, name='profile_edit'), # Profile Update
    path('<str:username>/', views.profile, name='profile'),
]