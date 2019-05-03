from django.urls import path
from .views import HomePageView, Index, Login, Profile

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
]
