from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
# from django.core.mail import send_mail
# import random


def index(request):
	return render(request, "index.html")


# def first(request):
#     return render(request, "first.html")


# def registr(request):
#     return render(request, 'registr.html')


def user_login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd["username"], password=cd["password"])
			if user is not None:
				if user.is_active:
					login(request, user)
					return index(request)
				else:
					return HttpResponse("Disabled account")
			else:
				return HttpResponse("Неверный логин или пароль")
	else:
		form = LoginForm()
	return render(request, "first.html", {"form": form})

# def generate_code():
# 	random.seed()
# 	return str(random.randint(10000,99999))

def register(request):
	if request.method == "POST":
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data["password"])
			# new_user.is_active = False
			# Save the User object
			new_user.save()
			# if new_user and new_user.is_active == False:
			# 		message = generate_code();
			# 		send_mail('код подтверждения', message, 'camagru21@rambler.ru', ['ilyashenko-vlad@mail.ru'], fail_silently=False) 
			# 		# new_user.email_user('код подтверждения', message, from_email=None)
			# 		login(request, new_user)
			# 		return redirect('/personalArea/')
			# else: #тут добавить редирект на страницу с формой для ввода кода.
			# 		return render(request, 'registration/register.html', {'form': form})
			# new_user.objects.create(username = user_form.username, email = user_form.email, password = user_form.cleaned_data["password"])
			return render(request, "register_done.html", {"new_user": new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, "registr.html", {"user_form": user_form})

