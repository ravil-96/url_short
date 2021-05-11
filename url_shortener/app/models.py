from django.db import models

# Create your models here.
class Url(models.Model):
    original = models.TextField()
    short_url = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.original}'
        # return f'Here is your short url: {self.short_url}.\n (Generated from original: {self.original}'


    