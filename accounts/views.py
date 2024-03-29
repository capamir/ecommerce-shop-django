from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm

    template_name = 'accounts/register.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'you registered successfully', 'success')
        return super().form_valid(form)


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('products:products')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = self._login_user(form.cleaned_data)
        if user is None:
            return self.form_invalid(form)            
        
        return super().form_valid(form)

    def _login_user(self, data):
        user = authenticate(self.request, 
                            email=data['email'], 
                            password=data['password'])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'you logged in successfully', 'info')
        else:
            messages.error(self.request, 'email or password is wrong', 'warning')

        return user

class UserLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = '/'
