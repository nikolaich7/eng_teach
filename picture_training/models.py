from django.contrib.auth.models import User
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=25)
    translation = models.TextField()
    studied = models.BooleanField(default='False')

    def __str__(self):
        return self.word


class Picture(models.Model):
    picture = models.ImageField(upload_to='%Y/%m/%d/')
    text = models.TextField()
    translation = models.TextField()
    words = models.ManyToManyField('Word')

    def __str__(self):
        return self.text


class WordsUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    words_repeat_often = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE,
                                           related_name='words_repeat_often')
    words_repeat = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE, related_name='words_repeat')
    words_repeat_rare = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE,
                                          related_name='words_repeat_rare')
    words_studied = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE, related_name='words_studied')
    words_use = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE, related_name='words_use')
