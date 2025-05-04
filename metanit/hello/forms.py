from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(label="Ваше имя",min_length=2, max_length=20)
    age = forms.IntegerField(help_text="Введите свой возраст", label="Ваш возраст",min_value=1, max_value=100)
    email = forms.EmailField(label="Ваша почта", help_text="в поле обязательно должен присутствовать символ @")
    about = forms.CharField(label="О себе", help_text="пару слов", required=False)
    required_css_class = "field"
    error_css_class = "error"

    #required=False
    
