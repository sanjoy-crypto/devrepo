from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register'),
    path('logout/', logoutUser, name='logout'),

    path('', profile, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('account/', userAccount, name='account'),
    path('edit-account/', editAccount, name='edit-account'),

    path('create-skill/', createSkill, name='create-skill'),
    path('update-skill/<str:pk>/', updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', deleteSkill, name='delete-skill'),
]
