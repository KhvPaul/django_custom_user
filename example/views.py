from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserForm, RegisterForm
from .models import User

# Create your views here.


class UserDetailView(generic.DetailView):
    model = User


class UserListView(generic.ListView):
    model = User


class RegisterFormView(generic.FormView):
    template_name = "example/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("example:user_list")

    def form_valid(self, form):
        user = form.save()

        user = authenticate(self.request, username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["first_name", "last_name", "email", "biography", "image"]
    template_name = "example/user_form.html"
    success_url = reverse_lazy("example:user_list")

    def get_object(self, queryset=None):
        user = self.request.user
        return user
