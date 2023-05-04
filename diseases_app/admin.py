from django.contrib import admin
from . models import HeartDiseasePrediction,KidneyDiseasePrediction,LiverDiseasePrediction,DiabetesDiseasePrediction
# Register your models here.
admin.site.register(HeartDiseasePrediction)
admin.site.register(KidneyDiseasePrediction)
admin.site.register(LiverDiseasePrediction)
admin.site.register(DiabetesDiseasePrediction)