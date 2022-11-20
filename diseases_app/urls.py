from django.urls import path
from .views import Heart_Disease_Prediction
urlpatterns=[

    path('heart/',Heart_Disease_Prediction,name="heart"),
]