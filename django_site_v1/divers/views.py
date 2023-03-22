from django.shortcuts import render

import requests

import json

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from . import forms

from .fonctions import analyse_sentiment_api_azure
from dotenv import load_dotenv

# Classe du SDK Azure qui fournit une méthode d'authentification à l'aide d'une clé API.
from azure.core.credentials import AzureKeyCredential

# Classe du SDK Azure qui permet d'accéder au service d'analyse de texte d'Azure,
from azure.ai.textanalytics import TextAnalyticsClient

import os

from .forms import ChampText

# Create your views here.
def home_view(request):
    return render(request, 'divers/formulaire.html')

def about_view(request):
    return render(request, 'divers/about_page.html')

class UserCreateView(CreateView):
    form_class = forms.UserCreationFormCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

def consumer(request):
    
    # Charge les variables d'environnement à partir du fichier .env
    load_dotenv('.env')

    # Point de terminaison et clé API
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    # Authentification de l'objet client
    text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

    champ_text = ChampText()

    sentiment = "error"
    if request.method == 'POST':
        client_text = request.POST.get('champ_text')
        sentiment = analyse_sentiment_api_azure(texte=client_text, api=text_analytics_client)

        context = {'champ_text':champ_text, 'sentiment':sentiment, 'client_text':client_text}

        return render (request=request, template_name="divers/formulaire.html", context=context)

    context = {'champ_text':champ_text}
    return render (request=request, template_name="divers/formulaire.html", context=context)
   
def consumer_azure(request):
    
    # Charge les variables d'environnement à partir du fichier .env
    load_dotenv('.env')

    # Point de terminaison et clé API
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    # Authentification de l'objet client
    text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

    champ_text = ChampText()

    sentiment = "error"
    if request.method == 'POST':
        client_text = request.POST.get('champ_text')
        sentiment = analyse_sentiment_api_azure(texte=client_text, api=text_analytics_client)

        context = {'champ_text':champ_text, 'sentiment':sentiment, 'client_text':client_text}

        return render (request=request, template_name="divers/formulaire.html", context=context)

    context = {'champ_text':champ_text}
    return render (request=request, template_name="divers/formulaire.html", context=context)
