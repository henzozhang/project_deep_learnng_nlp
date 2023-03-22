from django.shortcuts import render

from .forms import ApiForm

import requests

import json

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from . import forms
# Create your views here.
def home_view(request):
    return render(request, 'divers/home_page.html')

def about_view(request):
    return render(request, 'divers/about_page.html')

class UserCreateView(CreateView):
    form_class = forms.UserCreationFormCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

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
            return render(request, 'divers/formulaire.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'divers/formulaire.html', context=context )
   
def consumer_azure(request):
    
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
            return render(request, 'divers/formulaire.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'divers/formulaire.html', context=context )