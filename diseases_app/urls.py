from django.urls import path
from .views import Heart_Disease_Prediction,dashboard
urlpatterns=[

    path('heart/',Heart_Disease_Prediction,name="heart"),
    path('dashboard/',dashboard,name='dashboard')
]