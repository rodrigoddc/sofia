from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "home/home.html"


class Index(TemplateView):

    template_name = "home/index.html"


class Profile(TemplateView):

    template_name = "home/profile-page.html"


class Login(LoginView):

    template_name = "home/registration/login.html"
