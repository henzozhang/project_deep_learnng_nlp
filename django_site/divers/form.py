from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class ChampText(forms.Form):
    champ_text = forms.CharField(label="Entrez votre texte", max_length=256, required=False)

    def __init__(self, *args, **kwargs):
        super(ChampText, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('champ_text', css_class='form-control', placeholder='Entrez votre texte')
        )