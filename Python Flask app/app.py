
from flask import Flask, render_template,flash
from forms import PredictionForm
import requests
from flask import json

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = '1bd9a9f3a7576f79712058c466bd7a93' #you will need a secret key

@app.route('/',methods=('GET','POST'))
def startApp():
    form = PredictionForm()
    return render_template('predictorForm.html',form=form)

@app.route('/predict',methods=('GET','POST'))
def predict():
    form = PredictionForm()
    if form.submit():
      # flash("Working",'success')
      header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
               + "eyJraWQiOiIyMDIwMDYyNDE4MzAiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTAxYmQwYmRhLWY2YmMtNDY0Yy1iMzA0LTI5MzUyZTlhZDA2ZSIsImlkIjoiaWFtLVNlcnZpY2VJZC0wMWJkMGJkYS1mNmJjLTQ2NGMtYjMwNC0yOTM1MmU5YWQwNmUiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC0wMWJkMGJkYS1mNmJjLTQ2NGMtYjMwNC0yOTM1MmU5YWQwNmUiLCJuYW1lIjoiU2VydmljZSBjcmVkZW50aWFscy0xIiwic3ViIjoiU2VydmljZUlkLTAxYmQwYmRhLWY2YmMtNDY0Yy1iMzA0LTI5MzUyZTlhZDA2ZSIsInN1Yl90eXBlIjoiU2VydmljZUlkIiwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiMjU2YWU1YjVmZjcxNGRiZDhjMDU1MDBhYjAxZTViNWMifSwiaWF0IjoxNTkzNDQ0MTY4LCJleHAiOjE1OTM0NDc3NjgsImlzcyI6Imh0dHBzOi8vaWFtLmJsdWVtaXgubmV0L2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.1d60axMyD9AZrZge3p_WHQsdfBH2EAqQs1k4B56uA8Gnn2VXJ3qnZS3cLCpBku2gj_Z2XY4FSlLa3TH3Aa98GZzM_FPsKzr-AVHvdA4Xa_sHq4w7Zg-MCniKE-l6_5_mHMJHNcpeVvhKOX2UqRUIzGe_79_DwOC5V24C9UXUb81SuYRO87u6jLu1JizEGkMtAU_QMZxo38gRuIOpWEZnJm5wIc4QIR4DOT0S2k6fvVypybE6UGwf3Oawr7OUogx_o8XgQ7cgY4rYyFTHo6YFTEk0ZmMIy39FkG_srof9jpn5CiNBEh6mp03L9kNVy5pe2LqM1qO2iw2hxG5A1S0OMw","refresh_token":"OKA_gdpog54U7jbh9N2oMTpdDUCAeTkE4WvhLbql0QDT1NHn-5It5d3dSzxjeHBSsfur1_q_FR40-mi6NEIWPlHhley7C6LfeHtYNn4fzepHpb51RifLBjsEYMFTXNjZMf2p0DmcT_zTh_maXRWThssNwZNIuNw4_7L8Kv_bqbL7bgzKBNXULk8QjPF-5bZ51S_vcLtUudJlbL62_FMbWKP9zSBAYoMBy3o208AXgdU8ikofjQXpttEseVNriWHw6Iz0P21OIzU4l21Psymwnol5VmierRM1IaxTddTkWH8IwmdIBM6R3coWbbblp4VNfRXSGxA3lUF2C6mqFdDoUviHxY5DoNVuLWzYVJOBhgek5EURHooSZ3TEce_30YQ6xVIdp8kO9wEM9wA8Iv--H0Bighr2ppiV-ENMBlIxyMsUfamTSRzdIsJaV9fJ46sAgNfHdGJDR1dT0zKAnh-2DFnyY0X0-BaiwLUjSeVEQ4X3OjYwoMGrqhpWWX9uSItDhvzUP8oUMtoB8PzJyCUGusDw6drUGOryW3JT08jHyC7jVh5ErjRtaC3toA2hP9XcwqAcllWSTykbte6YkO_10Iz-lbf9fi5r9dbGOsFVfaYTvMgI3dRQLsX64dghEDlmo5okifitDag1QHKk72cUfnxWNaYaaiCa30DtIs8wmSsIb_LUUAzpEerMXCgqJHAllKek2bL96hn9ytkzZdc_tvkPdAS_6U_uNoozjXHExGNySEcozdnfIU4DrXlkRfUIQ3qS3cHUkrkbSp-49ohqUfwiyNox35ElhbCpC9ArP5jdDXdNMIRqDxWqfayvyneViEDCUaV_sQ1yk7MidDy0jmq-73jejWMlEuiaMbxC74WLDKj5HYj0K8c_rsgLtTzSiX2WktAQvXAdR0uL3l-d6IG-YWxnDxbHMNIcu1U0WAlzrCQzQHFYCuKsKOPclc5K2rvU88M-LsrvM60QPkbywx4_oAunkP7ArimKHmAbWfM5dj4pMTp51-VfaULhWydJvy4r3dBDEMrWbVRQuUikfW4p0DHx_ehQI6aBUquxTcFe7A",
                'ML-Instance-ID': "28607ee8-f59c-42a8-87e7-5941b3198461 "}
      if(form.country.data == None): 
        python_object = []
      else:
        python_object = [form.country.data,form.year.data,form.status.data,form.adult_mortality.data,form.infant_deaths.data,form.alcohol.data,form.percentage_expenditure.data,form.hepatitis_b.data,form.measles.data,form.bmi.data,form.under_five_deaths.data,form.polio.data,form.total_expenditure.data,form.diphtheria.data,form.hiv.data,form.gdp.data,form.population.data,form.thinness_1_to_19_years.data,form.thinness_5_to_9_years.data,form.income.data,form.schooling.data]
      
      #Transform python objects to  Json
      userInput = []
      userInput.append(python_object)
      # NOTE: manually define and pass the array(s) of values to be scored in the next line
      payload_scoring = {"input_data": [{"fields": ["Country", "Year", "Status", "Adult Mortality", "infant deaths", "Alcohol", "percentage expenditure", "Hepatitis B", "Measles ", " BMI ", "under-five deaths ", "Polio", "Total expenditure", "Diphtheria ", " HIV/AIDS", "GDP", "Population", " thinness  1-19 years", " thinness 5-9 years", "Income composition of resources", "Schooling"], "values": userInput}]}
      
      
      response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/v4/deployments/0447057f-d7e7-47b0-a45e-3c33baedd315/predictions', json=payload_scoring, headers=header)
      print("Scoring response")
      print(json.loads(response_scoring.text))
      response_scoring = requests.post("https://eu-gb.ml.cloud.ibm.com/v4/deployments/0447057f-d7e7-47b0-a45e-3c33baedd315/predictions", json=payload_scoring, headers=header)
  
      output = json.loads(response_scoring.text)
      print(output)
      for key in output:
        ab = output[key]
      print(ab)  
      for key in ab[0]:
        bc = ab[0][key]
      print(bc)
      roundedExpectancy = round(bc[0][0],2)
      print(roundedExpectancy)
      form.abc = roundedExpectancy # this returns the response back to the front page
      return render_template('predictorForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
