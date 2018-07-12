from django import forms
from django.forms import ModelForm,Textarea
from .models import Profile,Test


class ProfileForm(forms.ModelForm):

	class Meta:
		model=Profile
		fields=['first_name','last_name','address','city','country','occupation','mobile_number']
		

class AboutForm(forms.ModelForm):
	about=forms.CharField(widget=forms.Textarea)
	class Meta:
		model=Profile
		fields=['image','about']

class TestForm(forms.ModelForm):
	class Meta:
		model=Test
		fields=['amount','level','category','q_type']

		labels = {
            'q_type': 'Questions Type',
        }