from django import forms
from django.forms import DateInput, NumberInput

from django.contrib.auth.forms import UserCreationForm
CHOICES = ((0,'Canceled'),(1,'Scheduled'),(2,'In Progress'),(3,'Done'),)

class FormUser1(UserCreationForm):
    # Atenção que 'username', 'email', 'passowrd1' e 'password2' são campos de tabelas do Django
    username = forms.CharField(label="Username",max_length=100, min_length=5)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password", widget=forms.PasswordInput)

class ProjectForm(forms.Form):
    _name = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '70'}),label="Project Name:", min_length=3, max_length=200, required=True)
    _notes = forms.CharField(widget=forms.Textarea(attrs={'cols':'73','rows':'9'}),label= "Project Notes:",required=False)
    _start_date = forms.DateTimeField(widget = DateInput(format='%d-%m-%Y'),
                                   input_formats=('%d-%m-%Y','%d/%m/%Y','%d.%m.%Y',),
                                   required=False, label="Start Date:")
    _end_date = forms.DateTimeField(widget = DateInput(format='%d-%m-%Y'),
                                   input_formats=('%d-%m-%Y','%d/%m/%Y','%d.%m.%Y',),
                                   required=False, label=" End Date:")
                                   
    _status = forms.ChoiceField(choices=CHOICES, label="Status:")

class TaskForm(forms.Form):
    _name = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '70'}),label="Task Name:", min_length=3, max_length=200, required=True)
    _value = forms.ChoiceField(choices=((1,'Insignificant'),(2,'Significant'),(3,'Important'),
    (4,'Relevant'),(5,'High!')), label="Value:")
    _urgency = forms.ChoiceField(choices=((1,'No date'),(2,'Postponable'),(3,'Urgent'),
    (4,'Very urgent'),(5,'Do it Now!')), label="Urgency:")
    _compliance = forms.ChoiceField(choices=((1,'None'),(2,'Applicable'),(3,'Impact'),
    (4,'Consequent'),(5,'Critical!')), label="Compliance:")
    _effort = forms.ChoiceField(choices=((1,'Easy'),(2,'Accessible'),(3,'Moderate'),
    (4,'Difficult'),(5,'Complex!')), label="Effort:")
    _cost = forms.IntegerField(widget=NumberInput(attrs={'min':0, 'max':1000000000, 'step':1,'value':0}),label="Cost:",required=True)
    _start_date = forms.DateTimeField(widget = DateInput(format='%d-%m-%Y'),
                                   input_formats=('%d-%m-%Y','%d/%m/%Y','%d.%m.%Y',),
                                   required=True, label="Start Date:")
    _end_date = forms.DateTimeField(widget = DateInput(format='%d-%m-%Y'),
                                   input_formats=('%d-%m-%Y','%d/%m/%Y','%d.%m.%Y',),
                                   required=True, label=" End Date:")
    _progress = forms.IntegerField(widget=NumberInput(attrs={'min':0, 'max':100, 'step':5,'value':0}),label="Progress:",required=True)
    _status = forms.ChoiceField(choices=CHOICES, label="Status:")
