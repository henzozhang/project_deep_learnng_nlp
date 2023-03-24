# Modules Django
from django.shortcuts import render

# Modules du projet
from . import forms
from .utils import call_api
from .fonctions import analyse_sentiment_api_azure

# Modules pour l'accès aux clés d'API
import os
from dotenv import load_dotenv

# Modules pour la date et l'heure
from datetime import datetime

# Modules pour l'analyse de texte Azure
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Modules pour les requêtes HTTP
import requests

# Modules OpenAI
import openai



# Charge les variables d'environnement à partir du fichier .env
load_dotenv('.env')

# Récupère la clé d'API OpenAI à partir des variables d'environnement
openai.api_key = os.getenv('API_KEY')

# Récupère l'URL de l'API et la clé d'API pour Azure Text Analytics à partir des variables d'environnement
endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]

# Crée un client pour Azure Text Analytics en utilisant les informations d'authentification 
text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

# Définit une URL d'API Hugging Face et un en-tête d'autorisation 
API_URL = "https://api-inference.huggingface.co/models/citizenlab/twitter-xlm-roberta-base-sentiment-finetunned"
headers = {"Authorization": "Bearer <API_token>"}



# Initialisation de la liste des messages et de la variable de saisie utilisateur
messages = []
user_prompt = ""

# Définition de la vue "chatbox"
def chatbox(request):

    # Création d'un formulaire d'entrée de texte utilisateur
    form = forms.InputForm(request.POST or None)

    # Initialisation de la variable de message utilisateur
    user_msg = None
    
    # Récupération de l'utilisateur connecté
    logged_in_user = request.user

    # Si le formulaire est valide
    if form.is_valid() :

        # Récupération du texte saisi par l'utilisateur
        user_msg = form.cleaned_data['text_msg']

        # Stockage du texte dans une variable "champ_text"
        champ_text = user_msg

        # Création d'un nouveau formulaire vide
        form = forms.InputForm()

        # Récupération de l'heure actuelle
        time = datetime.today().strftime('%H:%M')

        # Appel de l'API pour l'analyse de sentiment du message utilisateur
        sentiment = "error"
        if request.method == 'POST':
            client_text = request.POST.get('champ_text')
            sentiment = analyse_sentiment_api_azure(texte=champ_text, api=text_analytics_client)
            print(sentiment)

        # Création du contexte pour le rendu de la vue
        context = {'champ_text':champ_text, 'sentiment':sentiment, 'client_text':client_text,'form': form, 'messages':messages, 'time': time}

        # Ajout du message utilisateur dans la liste "messages"
        messages.append({user_msg : sentiment})

        # Ajout d'un message par défaut 
        messages.append({"" : "Désolé je n'ai pas compris votre questions merci de la reformuler"})

        # Rendu de la vue
        return render(request, "chatbox/chatbox.html", context=context)
    
    else:

        # Si l'utilisateur est connecté, on supprime tous les messages précédents et on ajoute un message de bienvenue
        if str(logged_in_user) != "AnonymousUser":
            messages.clear()
            messages.append({"": f"Hello {logged_in_user}, how are you doing today ?"})

        else:

            # Si l'utilisateur n'est pas connecté, on supprime tous les messages précédents
            messages.clear()

        # Rendu de la vue
        return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})


def chatbox2(request):

    form = forms.InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
   

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
    