from django import forms

class Formulario(forms.Form):
    varietal = forms.CharField()
    origen = forms.CharField()
    fecha = forms.DateField()
    temperatura = forms.IntegerField()