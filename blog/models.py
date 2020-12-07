from django.db import models
from django.utils import timezone
class Post (models.Model):
	title = models.CharField(max_length = 50)
	text = models.TextField()
	created_data = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(null = True, blank = True)

	def publish(self):
		self.published_date = timezone.now()
