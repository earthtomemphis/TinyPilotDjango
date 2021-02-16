from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, ValidationError
from .models import User

# Create your views here.


# @login_required
def index(request):
    return render(request, 'index.html', {})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form':  AuthenticationForm})

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'login.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('dashboard'))


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.filter(username=request.user).all()
        return render(request, 'dashboard.html', {'users': users})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html', {})
