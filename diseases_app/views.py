from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HeartDiseasePrediction
from django.contrib import messages
# Create your views here.
import numpy
import joblib
from django.core.mail import send_mail

@login_required
def Heart_Disease_Prediction(request):
    heart_model = joblib.load('data_science\heart\model.pkl')

    result = None
    predicted_result_for_heart_disease = None
    if request.method == "POST":
        user = request.user
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        chest_pain_type = request.POST.get('chest_pain_type')
        resting_bp = request.POST.get('resting_bp')
        cholestrol = request.POST.get('cholestrol')
        fasting_blood_sugar = request.POST.get('fasting_blood_sugar')
        resting_electrocardiographic_results = request.POST.get(
            'resting_electrocardiographic_results')
        thalach = request.POST.get('thalach')
        exercise_included_angina = request.POST.get('exercise_included_angina')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')

        features = [age, sex, chest_pain_type, resting_bp, cholestrol, fasting_blood_sugar,
                    resting_electrocardiographic_results, thalach, exercise_included_angina, oldpeak, slope, ca, thal]

        float_conversion = [float(val) for val in features]

        prediction_features = [numpy.array(float_conversion)]

        prediction = heart_model.predict(prediction_features)
        predicted_result_for_heart_disease = prediction[0]
        prediction = HeartDiseasePrediction.objects.create(
            user=user, age=age, sex=sex, chest_pain_type=chest_pain_type, resting_bp=resting_bp, cholestrol=cholestrol,
            fasting_blood_sugar=fasting_blood_sugar, resting_electrocardiographic_results=resting_electrocardiographic_results, thalach=thalach, exercise_included_angina=exercise_included_angina, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, predicted_result_for_heart_disease=predicted_result_for_heart_disease)

        # prediction = prediction.save()
        prediction.save()
        print(predicted_result_for_heart_disease,prediction)
        messages.success(request, "Predicted Successfully!!!")

    context = {
        'result': result,
        'predicted_result':predicted_result_for_heart_disease
    }
    return HttpResponse("Result")

def dashboard(request):
    return render(request,'dashboard.html')


