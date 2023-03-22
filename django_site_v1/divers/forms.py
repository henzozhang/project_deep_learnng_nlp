from django import forms


from django.contrib.auth.forms import UserCreationForm
from . import models

class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ['username', 'email']

# class ApiForm(forms.Form):
#     votre_question = forms.CharField(max_length=200)
    # bankstate = forms.ChoiceField(choices=STATES,initial='IN')
    # term = forms.IntegerField(initial=180)
    # noemp = forms.IntegerField(initial=7)
    # newexist = forms.ChoiceField(choices=ITEMS,initial='yes')
    # createjob = forms.IntegerField(initial=0)
    # retainedjob = forms.IntegerField(initial=0)
    
    # franchisecode = forms.ChoiceField(choices=ITEMS1,initial='N')
    # urbanrural = forms.ChoiceField(choices=ITEMS,initial='yes')
    # revlinecr = forms.ChoiceField(choices=ITEMS1,initial='N')
    # lowdoc = forms.ChoiceField(choices=ITEMS1,initial='N')
    # grappv = forms.IntegerField(initial=287000)

class ChampText(forms.Form):
    champ_text = forms.CharField(label="Entrez votre texte", max_length=256, required=False)