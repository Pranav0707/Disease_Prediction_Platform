# Generated by Django 4.1 on 2022-11-20 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartDiseasePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tested_at', models.DateTimeField(auto_now_add=True)),
                ('age', models.CharField(max_length=255, null=True)),
                ('sex', models.CharField(max_length=255, null=True)),
                ('chest_pain_type', models.CharField(max_length=255, null=True)),
                ('resting_bp', models.CharField(max_length=255, null=True)),
                ('cholestrol', models.CharField(max_length=255, null=True)),
                ('fasting_blood_sugar', models.CharField(max_length=255, null=True)),
                ('resting_electrocardiographic_results', models.CharField(max_length=255, null=True)),
                ('thalach', models.CharField(max_length=255, null=True)),
                ('exercise_included_angina', models.CharField(max_length=255, null=True)),
                ('oldpeak', models.CharField(max_length=255, null=True)),
                ('slope', models.CharField(max_length=255, null=True)),
                ('ca', models.CharField(max_length=255, null=True)),
                ('thal', models.CharField(max_length=255, null=True)),
                ('predicted_result_for_heart_disease', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
