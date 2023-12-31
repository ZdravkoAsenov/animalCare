from django.urls import path, include

from animal.views import CreateAnimalView, AnimalListView, AnimalEditView, AnimalDetailView, \
    delete_animal, animal_save_hour, SavedAnimalListView, EditSavedAnimalView, SavedAnimalDeleteView, examination_list, \
    AddExamination, user_examinations

urlpatterns = [
    path('', include([
        path('<int:pk>/', AnimalDetailView.as_view(), name='detail animal'),
        path('create/', CreateAnimalView.as_view(), name='create animal'),
        path('list/', AnimalListView.as_view(), name='list animal'),
        path('<int:pk>/update/', AnimalEditView.as_view(), name='edit animal'),
        path('<int:pk>/delete/', delete_animal, name='delete animal'),
        path('<int:animal_pk>/save_hour/', animal_save_hour, name='save hour animal'),
        path('saved-animal/', SavedAnimalListView.as_view(), name='saved animal hour detail'),
        path('saved-animal/<int:animal_pk>/edit/', EditSavedAnimalView.as_view(), name='saved animal hour edit'),
        path('saved-animal/<int:animal_pk>/delete/', SavedAnimalDeleteView.as_view(), name='saved animal hour delete'),
        path('examinations/', examination_list, name='list examination'),
        path('examinations/add/<int:user_pk>/<int:animal_pk>/', AddExamination.as_view(), name='add examination'),
        path('user_examinations/', user_examinations, name='user examinations'),
    ]))
]