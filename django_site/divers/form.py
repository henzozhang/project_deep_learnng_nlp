from django import forms
from django import forms

STATES = [    ('IN', 'Indiana'),    ('OK', 'Oklahoma'),    ('FL', 'Florida'),    ('CT', 'Connecticut'),    ('NJ', 'New Jersey'),    ('NC', 'North Carolina'),    ('IL', 'Illinois'),    ('RI', 'Rhode Island'),    ('TX', 'Texas'),    ('VA', 'Virginia'),    ('TN', 'Tennessee'),    ('AR', 'Arkansas'),    ('MN', 'Minnesota'),    ('MO', 'Missouri'),    ('MA', 'Massachusetts'),    ('CA', 'California'),    ('SC', 'South Carolina'),    ('LA', 'Louisiana'),    ('IA', 'Iowa'),    ('OH', 'Ohio'),    ('KY', 'Kentucky'),    ('MS', 'Mississippi'),    ('NY', 'New York'),    ('MD', 'Maryland'),    ('PA', 'Pennsylvania'),    ('OR', 'Oregon'),    ('ME', 'Maine'),    ('KS', 'Kansas'),    ('MI', 'Michigan'),    ('AK', 'Alaska'),    ('WA', 'Washington'),    ('CO', 'Colorado'),    ('MT', 'Montana'),    ('WY', 'Wyoming'),    ('UT', 'Utah'),    ('NH', 'New Hampshire'),    ('WV', 'West Virginia'),    ('ID', 'Idaho'),    ('AZ', 'Arizona'),    ('NV', 'Nevada'),    ('WI', 'Wisconsin'),    ('NM', 'New Mexico'),    ('GA', 'Georgia'),    ('ND', 'North Dakota'),    ('VT', 'Vermont'),    ('AL', 'Alabama'),    ('NE', 'Nebraska'),    ('SD', 'South Dakota'),    ('HI', 'Hawaii'),    ('DE', 'Delaware'),    ('DC', 'District of Columbia')]



ITEMS = [    ('non', 'No'),    ('yes', 'Yes'),    ('nd', 'Not defined'),]
ITEMS1 = [    ('N', 'No'),    ('Y', 'Yes'),]


class ApiForm(forms.Form):
    state = forms.ChoiceField(choices=STATES,initial='IN')
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