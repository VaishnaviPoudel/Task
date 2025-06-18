from django import forms

from .models import WaterIntake, WaterIntakeGoal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntake
        fields = ['amount']

    CHOICES = [
        (200,'200 ml'), 
        (250,' 250 ml'),
        (300, '300 ml'),  
        (500,'500 ml'),
        (750, '750 ml'), 
        (1000,' 1 litre' )
        ]

    amount = forms.ChoiceField(
            choices=CHOICES, 
            label='select amount' ,
            widget  = forms.Select(attrs={'class':'form-control'})
    )


class WaterIntakeGoalForm(forms.ModelForm):
    class Meta:
        model = WaterIntakeGoal
        fields = ['daily_goal_amount']
        labels = {'Water Intake Goal': 'Daily Goal (in ml)'}
        widgets = {
                    'daily_goal_amount': forms.NumberInput(attrs={
                        'placeholder': 'e.g. 2000 ml',
                        'class': 'form-control',
                        
                    })}

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
