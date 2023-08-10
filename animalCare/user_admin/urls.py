from django.urls import path, include

from user_admin.views import home_administration, user_list, AdminUserDetailView, \
    AdminAnimalListView, AdminAnimalDetailView, AdminExaminationListView, AdminExaminationDetailView, \
    unanswered_contacts, mark_contact_answered, answered_contacts

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
    path('contacts/', include([
        path('unanswered', unanswered_contacts, name='unanswered inquiries'),
        path('mark_answered/<int:pk>/', mark_contact_answered, name='mark inquiries answered'),
        path('answered/', answered_contacts, name='answered inquiries'),
    ])),
]
