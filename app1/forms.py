from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=30)
    comision = forms.IntegerField()
    detalle = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

#class EstudianteFormulario(forms.Form):
#    nombre = forms.CharField(max_length=30)
#    apellido = forms.CharField(max_length=30)
#    email = forms.EmailField()

#class ProfesorFormulario(forms.Form):
#    nombre = forms.CharField(max_length=30)
#    apellido = forms.CharField(max_length=30)
#    email = forms.EmailField()
#    profesion = forms.CharField(max_length=30)

#class EntregableFormulario(forms.Form):
#    nombre = forms.CharField(max_length=30)
#    fecha_de_entrega = forms.DateField()
#    entregado = forms.BooleanField()

#class BuscarFormulario(forms.Form):
#    comision = forms.IntegerField(required=False)