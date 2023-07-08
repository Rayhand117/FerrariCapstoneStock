from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField,FloatField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   Date = StringField('Date')
   High = FloatField('High')
   Low = FloatField('Low')
   Close = FloatField('Close')
   AdjClose = FloatField('Adj Close')
   Volume = IntegerField('Volume')
   submit = SubmitField('Predict')
   abc = "" # this variable is used to send information back to the front page
# "Date", "High", "Low", "Close", "Adj Close", "Volume"