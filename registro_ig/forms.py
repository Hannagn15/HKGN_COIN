from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError

class MovementsForm(FlaskForm):
    date = DateField('Fecha', validators=[ DataRequired(message="La fecha es requerida") ])
    hora = StringField('Hora',validators=[DataRequired("El concepto es requerido")])
    moneda_from = FloatField('moneda_from',validators=[DataRequired(message="La cantidad es requerida, debe ser mayor a 0")])
    cantidad_from = FloatField('cantidad_from', validators=[ DataRequired(message="la cantidad es es requerida") ])
    moneda_to = FloatField('moneda_to', validators=[ DataRequired(message="La canitidad es requerida") ])
    cantidad_to = FloatField('moneda_to', validators=[ DataRequired(message="La cantidad es requerida") ])
    
    submit = SubmitField('Aceptar')

    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("fecha invalida: La fecha introducida es a futuro")