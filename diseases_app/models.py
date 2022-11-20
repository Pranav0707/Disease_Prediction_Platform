from django.db import models
from django .contrib.auth.models import User
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