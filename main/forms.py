from django import forms
from .models import TestEntry, Photo

class EntradaTeste(forms.ModelForm):

	class Meta:

		model = TestEntry
		fields = ['test_nome', 'test_topic', 'test_sumary']


class UploadImage(forms.ModelForm):

	class Meta:

		model = Photo
		fields = ['legenda', 'photo']
