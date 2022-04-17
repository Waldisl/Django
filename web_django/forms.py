from django						import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(widget= forms.TextInput
		(attrs={'class':'some_class', 'id':'username', 'placeholder' : 'Логин'}))
	password = forms.CharField(widget= forms.PasswordInput
		(attrs={'class':'some_class', 'id':'password', 'placeholder' : 'Пароль'}))

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput
		(attrs={'class':'some_class', 'id':'password', 'placeholder' : 'Пароль'}))
	password2 = forms.CharField(widget= forms.PasswordInput
		(attrs={'class':'some_class', 'id':'rep_pass', 'placeholder' : 'Повторите пароль'}))
	username = forms.CharField(widget= forms.TextInput
		(attrs={'class':'some_class', 'id':'username', 'placeholder' : 'Введите логин'}))
	email = forms.CharField(widget= forms.EmailInput
		(attrs={'class':'some_class', 'id':'email', 'placeholder' : 'Элетронная почта'}))

	def compare_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			self.add_error('password', 'Пароли не совпадают')
			return False
		return True




	class Meta:
		model = User
		fields = ('username', 'email')




