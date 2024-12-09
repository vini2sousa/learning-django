from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200);
    date = models.DateField(auto_created=True);

    def __str__(self):
        return self.text;

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE);
    text = models.TextField();
    date = models.DateField(auto_created=True);
    def __str__(self):
        return self.text;
