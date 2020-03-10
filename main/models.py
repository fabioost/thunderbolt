from django.db import models

# Create your models here.
class TestEntry(models.Model):
	test_nome = models.CharField(max_length=200)
	test_topic = models.CharField(max_length=200)
	test_sumary = models.TextField(max_length=200)
	test_number = models.IntegerField(default=0)
	test_test = models.BooleanField(default=True)

	def __str__(self):
		return self.test_nome