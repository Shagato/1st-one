from django.urls import path
from .views  import realtor

urlpatterns= [
    path('',realtor,name='realtor'),
]