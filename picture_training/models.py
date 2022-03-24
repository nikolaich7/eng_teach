from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=25)
    translation = models.TextField()

    def __str__(self):
        return self.word


class Picture(models.Model):
    picture = models.ImageField(upload_to='%Y/%m/%d/')
    text = models.TextField()
    translation = models.TextField()
    words = models.ManyToManyField('Word')

    def __str__(self):
        return self.text
