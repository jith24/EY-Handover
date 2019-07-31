from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    file = models.FileField(upload_to='files/', default='files/None/no-file.txt')
    published_date = models.DateTimeField(blank=True, null=True)
    pub = models.CharField(max_length=20)
    SHIFT_CHOICES = [
        ("D", "Day Shift"),
        ("N", "Night Shift"),
    ]
    shift_choices = models.CharField(
        max_length=1,
        choices=SHIFT_CHOICES,
        default="D",
    )
    def publish(self):
        self.published_date = timezone.now()
	self.pub = date.today()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def publish(self):
		self.save()
	def __str__(self):
		return self.name
