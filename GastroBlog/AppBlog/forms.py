from django import forms

class VinoFormulario(forms.Form):
    varietal = forms.CharField()
    origen = forms.CharField()
    fecha = forms.DateField(input_formats='%Y')
    temperatura = forms.IntegerField()