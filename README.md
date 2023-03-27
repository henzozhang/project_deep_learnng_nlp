

# POC : Analyse de sentiment dans une simulation de chatbot bancaire

## Description

Ce projet est une preuve de concept pour l'utilisation de l'analyse de sentiment dans un chatbot bancaire.\
L'objectif est d'améliorer l'expérience client en détectant les émotions négatives et en redirigeant les conversations vers un conseiller en direct si nécessaire.\
L'historique de la conversation est enregistré et envoyé par email.\
Ce processus vise également à préserver la réputation de la banque en évitant que les clients insatisfaits ne laissent de mauvaises évaluations.







## Badges

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](http://analyse-sentiment-nlp.c7f0f2c4cvcxd6hh.francecentral.azurecontainer.io/)

[![Work in Progress](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)](https://github.com/henzozhang/project_deep_learnng_nlp)


## Installation 

Lorsque vous clonez le répository sur votre machine, vous devez créer un environnement virtuel et installer les packages nécessaires: 

```bash
# Clonez le repository
git clone https://github.com/henzozhang/project_deep_learnng_nlp.git

# Accédez au répertoire du projet à partir de l'endroit où vous avez cloner le projet
cd nom_de_votre_projet

# Créez un environnement virtuel à la racine du répertoire contenant le projet
python -m venv env

# Activez l'environnement virtuel
source env/bin/activate

# Installez les packages nécessaires
pip install -r requirements.txt 
```
    
## Exécuter l'application localement

A la racine du répertoire contenant l'application Django, il faut :
- créer un fichier .env et ajouter dedans les lignes suivantes en remplaçant les exemples par vos propres clés.

```bash
SECRET_KEY=exemple_secret_key_value
AZURE_LANGUAGE_KEY=exemple_azure_language_key_value
AZURE_LANGUAGE_ENDPOINT=exemple_azure_language_endpoint_value
API_KEY=exemple_open_ai_key_value
```

Dans le même répertoire, contenant le fichier manage.py, utiliser les commandes suivantes pour appliquer les migrations à la base de données et lancer le serveur django:

```bash
# Générez les migrations
python manage.py makemigrations

# Appliquez les migrations à la base de données
python manage.py migrate

# Lancez l'application sur votre machine locale
python manage.py runserver
```






##  Jira et méthode agile

L'équipe a créé une liste de tâches sur Jira pour le POC et s'est assurée qu'elles sont correctement répertoriées, attribuées et validées.\
Le projet s'est déroulé sur deux semaines, divisé en quatre sprint.
## Documentation

[Définition et principe du NLP](https://datascientest.com/introduction-au-nlp-natural-language-processing)

[Azure Cognitives Services - API textanalytics](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/overview)



