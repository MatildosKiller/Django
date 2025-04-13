from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField( label="Ваше имя")
    age = forms.IntegerField(help_text="Введите свой возраст", label="Ваш возраст")
    
