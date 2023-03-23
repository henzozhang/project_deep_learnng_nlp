from django.shortcuts import render
from . import forms
import os
from datetime import datetime
import openai
from dotenv import load_dotenv
from .utils import call_api
from .fonctions import analyse_sentiment_api_azure

# Classe du SDK Azure qui fournit une méthode d'authentification à l'aide d'une clé API.
from azure.core.credentials import AzureKeyCredential

# Classe du SDK Azure qui permet d'accéder au service d'analyse de texte d'Azure,
from azure.ai.textanalytics import TextAnalyticsClient

import requests
import json



# Charge les variables d'environnement à partir du fichier .env
load_dotenv('.env')

openai.api_key = os.getenv('API_KEY')

# Point de terminaison et clé API
endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]

# Authentification de l'objet client
text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

API_URL = "https://api-inference.huggingface.co/models/citizenlab/twitter-xlm-roberta-base-sentiment-finetunned"
headers = {"Authorization": "Bearer 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"}


messages = []
user_prompt = ""


def chatbox(request):

    form = forms.InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
    
    # my_form = form.save(commit=False)
    # my_form.user= request.user
    # my_form.save()
    
    if form.is_valid() :
       
        user_msg = form.cleaned_data['text_msg']    
        champ_text = user_msg
        form = forms.InputForm()
        time = datetime.today().strftime('%H:%M')
        
       
        form = forms.InputForm()
        
        sentiment = "error"
        if request.method == 'POST':
            client_text = request.POST.get('champ_text')
            sentiment = analyse_sentiment_api_azure(texte=champ_text, api=text_analytics_client)
            print(sentiment)
            context = {'champ_text':champ_text, 'sentiment':sentiment, 'client_text':client_text,'form': form, 'messages':messages, 'time': time}
        
        messages.append({user_msg : sentiment})
        messages.append({"" : "Désolé je n'ai pas compris votre questions merci de la reformuler"})
    
        return render(request, "chatbox/chatbox.html", context=context)

    else:
        if str(logged_in_user) != "AnonymousUser":
            messages.clear()
            messages.append({"": f"Hello {logged_in_user}, how are you doing today ?"})
        else:
            messages.clear()
        return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})


def chatbox2(request):

    form = forms.InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
    # my_form = form.save(commit=False)
    # my_form.user= request.user
    # my_form.save()

    if form.is_valid() :
       
        user_msg = form.cleaned_data['text_msg']    
        form = forms.InputForm()
        time = datetime.today().strftime('%H:%M')
        
        form = forms.InputForm()

        sentiment = "error"
        if request.method == 'POST':
            payload={"inputs": user_msg}
            response = requests.post(API_URL, headers=headers, json=payload)
            print(response)
            if response.status_code == 503:
                sentiment = "Le modèle n'est pas accessible car actuellement en chargement dans le serveur de Hugging Face API"
            else:
                sentiment = response.json()

            context = {'sentiment':sentiment, 'form': form, 'messages':messages, 'time': time}

        messages.append({user_msg : sentiment})
        messages.append({"" : "Désolé je n'ai pas compris votre questions merci de la reformuler"})
    
        return render(request, "chatbox2/chatbox2.html", context=context)

    else:
        if str(logged_in_user) != "AnonymousUser":
            messages.clear()
            messages.append({"": f"Hello {logged_in_user}, how are you doing today ?"})
        else:
            messages.clear()
        return render(request, "chatbox2/chatbox2.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})
    