from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=30)
    comision = forms.IntegerField()
    detalle = forms.CharField(max_length=3000)