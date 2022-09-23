from django import forms

class CrearUsuario(forms.Form):
    user = forms.CharField(max_length=30)
    contraseña = forms.CharField(max_length=30)
    email = forms.EmailField()
    