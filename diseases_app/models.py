from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HeartDiseasePrediction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tested_at=models.DateTimeField(auto_now_add=True)
    age=models.CharField(max_length=255,null=True)
    sex=models.CharField(max_length=255,null=True)
    chest_pain_type=models.CharField(max_length=255,null=True)
    resting_bp=models.CharField(max_length=255,null=True)
    cholestrol=models.CharField(max_length=255,null=True)
    fasting_blood_sugar=models.CharField(max_length=255,null=True)
    resting_electrocardiographic_results=models.CharField(max_length=255,null=True)
    thalach=models.CharField(max_length=255,null=True)
    exercise_included_angina=models.CharField(max_length=255,null=True)
    oldpeak=models.CharField(max_length=255,null=True)
    slope=models.CharField(max_length=255,null=True)
    ca=models.CharField(max_length=255,null=True)
    thal=models.CharField(max_length=255,null=True)
    predicted_result_for_heart_disease=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.user.username + "heart results at" + self.tested_at
    
class KidneyDiseasePrediction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tested_at=models.DateTimeField(auto_now_add=True)
    blood_pressure=models.CharField(max_length=255,null=True)
    specific_gravity=models.CharField(max_length=255,null=True)
    albumin=models.CharField(max_length=255,null=True)
    sugar_degree=models.CharField(max_length=255,null=True)
    red_blood_cells=models.CharField(max_length=255,null=True)
    blood_glucose_random=models.CharField(max_length=255,null=True)
    blood_urea=models.CharField(max_length=255,null=True)
    serum_creatinine=models.CharField(max_length=255,null=True)
    sodium=models.CharField(max_length=255,null=True)
    potassium=models.CharField(max_length=255,null=True)
    heamoglobin=models.CharField(max_length=255,null=True)
    packed_ceel_volume=models.CharField(max_length=255,null=True)
    white_blood_cell_volume=models.CharField(max_length=255,null=True)
    red_blood_cell_count=models.CharField(max_length=255,null=True)
    appetite=models.CharField(max_length=255,null=True)
    anemia=models.CharField(max_length=255,null=True)
    predicted_result_for_kidney_disease=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.user.username + "kidney results at" + self.tested_at