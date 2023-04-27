from django.urls import path
from .views import Heart_Disease_Prediction_View,dashboard,Diabetes_Disease_Prediction_View,Kidney_Disease_Prediction_View,Liver_Disease_Prediction_View,Heart_Details,Liver_Details,Kidney_Details,Diabetes_Details
urlpatterns=[

    path('heart/',Heart_Disease_Prediction_View,name="heart"),
    path('liver/',Liver_Disease_Prediction_View,name="liver"),
    path('diabetes/',Diabetes_Disease_Prediction_View,name="diabetes"),
    path('kidney/',Kidney_Disease_Prediction_View,name="kidney"),
    path('heart_details/',Heart_Details,name="heartDetails"),
    path('liver_details/',Liver_Details,name="liverDetails"),
    path('kidney_details/',Kidney_Details,name="kidneyDetails"),
    path('diabetes_details/',Diabetes_Details,name="diabetesDetails"),
    path('dashboard/',dashboard,name='dashboard')
]