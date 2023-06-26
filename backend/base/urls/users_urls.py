from django.urls import path
from base.views import users_views

urlpatterns = [
    path('', users_views.getUsers, name='users'),

    path('login/', users_views.MyTokenObtainPairView.as_view(), name='my-token'),

    path('register/', users_views.registerUser, name='register'),

    path('profile/', users_views.getUserProfile, name='user-profile'),
    path('profile/update/', users_views.updateUserProfile, name='user-profile-update'),

]
