from django.urls import path
from .views import dane_list


urlpatterns = [
    path('missed/', dane_list)
]