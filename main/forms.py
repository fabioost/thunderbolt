from django import forms
from .models import TestEntry

class EntradaTeste(forms.ModelForm):

	class Meta:

		model = TestEntry
		fields = ['test_nome', 'test_topic', 'test_sumary']
