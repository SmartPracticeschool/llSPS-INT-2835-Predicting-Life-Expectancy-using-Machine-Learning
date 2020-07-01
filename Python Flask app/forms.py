from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    country = StringField('Country')
    year = IntegerField('Year')
    status = StringField('Status')
    adult_mortality = IntegerField('Adult Mortality')
    infant_deaths = IntegerField('infant deaths')
    alcohol = IntegerField('Alcohol')
    percentage_expenditure = IntegerField('percentage expenditure')
    hepatitis_b = IntegerField('Hepatitis B')
    measles = IntegerField('Measles ')
    bmi = IntegerField(' BMI ')
    under_five_deaths = IntegerField('under-five deaths ')
    polio = IntegerField('Polio')
    total_expenditure = IntegerField('Total expenditure')
    diphtheria = IntegerField('Diphtheria ')
    hiv = IntegerField(' HIV/AIDS')
    gdp = IntegerField('GDP')
    population = IntegerField('Population')
    thinness_1_to_19_years = IntegerField(' thinness  1-19 years')
    thinness_5_to_9_years = IntegerField(' thinness 5-9 years')
    income = IntegerField('Income composition of resources')
    schooling = IntegerField('Schooling')
    submit = SubmitField('Predict')
    abc = ""
