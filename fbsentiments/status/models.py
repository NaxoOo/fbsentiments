from django.db import models

# Create your models here.
class Profile(models.Model):
	profile_id = models.CharField(max_length=200)

	#def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class App(models.Model):
	app_id = models.CharField(max_length=200)
	app_secret = models.CharField(max_length=200)