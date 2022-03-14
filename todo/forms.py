from django import forms
from .models import *


class newTask(forms.ModelForm):

	class Meta:
		model = task
		fields = (
			'priority',
			'title',
			'due_date',
			'due_time',
			'notes',
		)

	title = forms.CharField(
		label='Description',
		required=True,
		max_length=50,
		widget=forms.TextInput(attrs={
			'cass': 'title',
			'placeholder': 'What do we have to do...'
		})
	)
	notes = forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={
			'class': 'notes',
			'placeholder': 'Short notes maybe...'
		}),
	)
	due_date = forms.DateField(
		required=False,
		widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
	)
	due_time = forms.TimeField(
		required=False,
		widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'})
	)
	priority = forms.ChoiceField(
		label='Priority',
		required=False,
		choices=priorities,
		widget=forms.RadioSelect(attrs={'class': 'priority'})
	)
