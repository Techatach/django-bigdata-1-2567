from django.shortcuts import render
#pip install joblib
#pip install scikit-learn
import joblib 

model = joblib.load('./modelAI/diabetes_model.pkl')

def predictor(request):
    if request.method == 'POST':
        Pregnancies = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        Age = request.POST['Age']
        y_pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
        return render(request, 'result.html', {'result':y_pred})
    return render(request, 'forms.html')


# model = joblib.load('./modelAI/lung_model.pkl')
# model1 = joblib.load(r'C:\Users\Taechatuch\Desktop\DjangoProject\projectd\modelAI\lung_model.pkl')

def predictLung(request):   
    if request.method == 'POST':               
        GENDER = request.POST['GENDER']
        AGE = request.POST['AGE']
        SMOKING = request.POST['SMOKING']
        YELLOW_FINGERS = request.POST['YELLOW_FINGERS']
        ANXIETY = request.POST['ANXIETY']
        
        # PEER_PRESSURE = request.POST['PEER_PRESSURE']
        # CHRONIC_DISEASE = request.POST['CHRONIC DISEASE']
        # FATIGUE = request.POST['FATIGUE']
        # ALLERGY = request.POST['ALLERGY']
        # WHEEZING = request.POST['WHEEZING']
        # ALCOHOL_CONSUMING = request.POST['ALCOHOL CONSUMING']
        # COUGHING = request.POST['COUGHING']
        # SHORTNESS_OF_BREATH	 = request.POST['SHORTNESS OF BREATH']
        # SWALLOWING_DIFFICULTY = request.POST['SWALLOWING DIFFICULTY']
        # CHEST_PAIN = request.POST['CHEST PAIN']
        # COUGHING = request.POST['COUGHING']
        # COUGHING = request.POST['COUGHING']
        
        y_pred = model1.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY]]) 
        return render(request, './cancer/result_cancer.html', {'result_cancer':y_pred})
    return render(request, './cancer/form_cancer.html')


# model2 = joblib.load('./modelAI/heart_model.pkl')

def predictHeart(request):   
    if request.method == 'POST':        
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
        
        y_pred = model2.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]) 
        return render(request, '/heart/result_heart.html', {'result_heart':y_pred})
    return render(request, '/heart/form_heart.html')
				
