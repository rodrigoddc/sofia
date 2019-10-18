from django.urls import path
from .views import HomePageView, Index, Profile

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', Index.as_view(), name='index'),
    path('profile/', Profile.as_view(), name='profile'),

]
