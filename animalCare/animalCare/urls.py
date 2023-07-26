from django.contrib import admin
from django.urls import path, include

from common import urls as common_urls
from profiles import urls as profiles_urls
from animal import urls as animal_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(common_urls)),
    path('profile/', include(profiles_urls)),
    path('animal/', include(animal_urls)),
]