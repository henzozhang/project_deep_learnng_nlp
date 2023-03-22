

def analyse_sentiment_api_azure(texte, api):
    """
    La fonction prend en entrée un texte, puis requête l'api textanalytics d'Azure Cognitive Services 
    pour l'analyser et retourne la prédiction en sortie
    """
    
    # Phrases à analyser
    documents = [texte]

    # Analyse de sentiments
    response = api.analyze_sentiment(documents)[0]

    if not response.is_error:
        sentiment = response.sentiment
    else:
        sentiment = "neutral"

    return sentiment