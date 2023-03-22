from django.shortcuts import render
from .fonctions import analyse_sentiment_api_azure
from dotenv import load_dotenv

# Classe du SDK Azure qui fournit une méthode d'authentification à l'aide d'une clé API.
from azure.core.credentials import AzureKeyCredential

# Classe du SDK Azure qui permet d'accéder au service d'analyse de texte d'Azure,
from azure.ai.textanalytics import TextAnalyticsClient

import os

from .form import ChampText

# Create your views here.
def home_view(request):

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

        return render (request=request, template_name="divers/home_page.html", context=context)

    context = {'champ_text':champ_text}
    return render (request=request, template_name="divers/home_page.html", context=context)



def consumer(request):
    
    form = ApiForm(request.POST or None)
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            
            data = json.dumps(form.cleaned_data)
            print(data)
            
            # reponse = requests.post('http://127.0.0.1:8000/predict', data=data)
            reponse = requests.post('https://bsa-api-model.onrender.com/predict', data=data)
            info = reponse.json()["mis_status"]
            if info == 'true':
                info = "Crédit Approuvé"
            else:
                info = "Crédit Refusé"
            return render(request, 'Mon_api/formulaire.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'Mon_api/formulaire.html', context=context )
