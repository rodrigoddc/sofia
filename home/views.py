from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "home/home.html"


class Index(TemplateView):

    template_name = "home/index.html"


class Profile(TemplateView):

    template_name = "home/profile-page.html"
