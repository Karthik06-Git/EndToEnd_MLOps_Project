import pandas as pd
import numpy as np
import math 
import locale
from src.ML_Project.pipeline.prediction import PredictionPipeline

from flask import Flask, render_template, request

# initializing falsk app
app = Flask(__name__)


# route to display the home-page
@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")




# route to show the predictions in the web
@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            # Get the Form data from HTML-page
            brand = str(request.form['brand'])
            year = int(request.form['year'])
            km_driven = int(request.form['km_driven'])
            fuel = str(request.form['fuel'])
            seller_type = str(request.form['seller_type'])
            transmission = str(request.form['transmission'])
            owner = str(request.form['owner'])

            # Create input DataFrame or reshape as needed
            input_data = pd.DataFrame({
                "brand": [brand], 
                "year": [year],
                "km_driven": [km_driven],
                "fuel": [fuel],
                "seller_type": [seller_type],
                "transmission": [transmission],
                "owner": [owner]
            })

            
            pipeline = PredictionPipeline()
            output = pipeline.predict(input_data)
            output = int(math.ceil(output / 1000.0)) * 1000

            # Formatting in Indian number system
            locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
            formatted_price = locale.format_string("₹ %d", output, grouping=True)

            return render_template('results.html', prediction=formatted_price)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)