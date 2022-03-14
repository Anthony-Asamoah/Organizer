from django.db import models
from django.utils import timezone

# Create your models here.

priorities = [(1, 'High'), (2, 'Medium'), (3, 'Low')]


class task(models.Model):
	priority = models.IntegerField(
		choices=priorities,
		null=True,
		blank=True,
	)
	title = models.CharField(
		null=False,
		max_length=50,
	)
	due_date = models.DateField(
		default=None,
		null=True,
		blank=True,
	)
	due_time = models.TimeField(
		default=None,
		null=True,
		blank=True,
	)
	notes = models.TextField(
		blank=True,
		null=True,
		help_text='Short notes'
	)
	completed = models.BooleanField(
		default=False,
		null=False,
	)
	completed_on = models.DateTimeField(
		default=None,
		null=True,
		blank=True,
	)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		ordering = ['priority', '-due_time', '-due_date', 'priority', 'title', 'completed_on']
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'
