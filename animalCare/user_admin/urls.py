from django.urls import path, include

from user_admin.views import home_administration, user_list, AdminUserDetailView,\
    AdminAnimalListView, AdminAnimalDetailView, AdminExaminationListView, AdminExaminationDetailView

urlpatterns = [
    path('', home_administration, name='home administration'),
    path('users/', include([
        path('', user_list, name='admin user list'),
        path('detail/<int:pk>/', AdminUserDetailView.as_view(), name='admin user detail'),
    ])),
    path('animal/', include([
        path('', AdminAnimalListView.as_view(), name='admin animal list'),
        path('<int:pk>/', AdminAnimalDetailView.as_view(), name='admin animal detail'),
    ])),
    path('examination/', include([
        path('', AdminExaminationListView.as_view(), name='admin exploration list'),
        path('<int:pk>/', AdminExaminationDetailView.as_view(), name='admin exploration detail'),
    ])),
]
