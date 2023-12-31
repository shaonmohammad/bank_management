from django.shortcuts import render
from django.views.generic import FormView
from . forms import UserRegistrationForms
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForms
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        print(form.cleanded_data)
        user = form.save()
        login(user)
        return super().form_valid(form)
