from flask import Flask, render_template, request
from sklearn.externals import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

#load model
mul_reg = open("multiple_linear_model.pkl", "rb")
ml_model = joblib.load(mul_reg)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/predict', methods=['GEt', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            NewYork = float(request.form['NewYork'])
            California = float(request.form['California'])
            Florida = float(request.form['Florida'])

            state = ''

            if NewYork == 1:
                state = 'New York'
            elif California == 1:
                state = 'California'
            elif Florida == 1:
                state = 'Florida'

            RnDSpend = float(request.form['RnDSpend'])
            AdminSpend = float(request.form['AdminSpend'])
            MarketSpend = float(request.form['MarketSpend'])

            pred_args = [NewYork, California, Florida, RnDSpend, AdminSpend, MarketSpend]

            pred_args_arr = np.array(pred_args)

            pred_args_arr = pred_args_arr.reshape(1, -1)

            model_pred = ml_model.predict(pred_args_arr)

            model_pred = [state, RnDSpend, AdminSpend, MarketSpend, round(float(model_pred), 2)]

        except ValueError:
            return "Please check if tha values are entered correctly"  
            
    return render_template('predict.html', prediction = model_pred)


if __name__ == "__main__":
    app.run(host='0.0.0.0')