from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
This options basically helps track number of days!
WEEK_DAYS = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)
'''
class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, unique=True)
	about = models.CharField(max_length = 500)
	banner = models.CharField(max_length=500)
	last_modified = models.DateField(auto_now=False)
	

	def __str__(self):
		return self.restaurant_name
