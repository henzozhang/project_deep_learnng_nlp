from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api_huggingface/', views.consumer, name='huggingface'),
    path('api_azurecognitive/', views.consumer_azure, name='azurecognitive'),
    path('about/', views.about_view, name='about'),
    # path('signup/', views.UserCreateView.as_view(), name='signup')

]