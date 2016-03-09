from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length=60)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True,auto_now_add=False)
	updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
	slug = models.SlugField(max_length=60)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
			super(Posts, self).save(*args, **kwargs)
