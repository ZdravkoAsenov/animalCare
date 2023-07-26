from django.urls import path

from profiles.views import ProfileCreateView, CustomLoginView, logout_view, profile_detail,\
    profile_edit, profile_delete

urlpatterns = [
    path('', profile_detail, name='detail profile'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='delete profile'),
    path('register/', ProfileCreateView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
