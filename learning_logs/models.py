from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200);
    date = models.DateField(auto_created=True);

    def __str__(self):
        return self.text;