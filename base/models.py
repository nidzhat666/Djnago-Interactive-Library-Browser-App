from django.db import models
from datetime import datetime
from django.utils import timezone
import os
import subprocess
from django.core.files import File


# Create your models here.

class Voiska(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return 'Voiska - ' + self.name + ' - ' + str(self.id)


class Voiska1(models.Model):
    name = models.CharField(max_length=150)
    voiska = models.ForeignKey(Voiska, on_delete=models.CASCADE)

    def __str__(self):
        return 'Voiska1 - ' + self.name + ' - ' + str(self.id)


class Ranks(models.Model):
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return 'Rank - ' + self.name + ' - ' + str(self.id)


class Author(models.Model):
    name = models.CharField(max_length=200, default='NONE')
    surname = models.CharField(max_length=200, default='NONE')
    father = models.CharField(max_length=200, default='NONE')
    rank = models.ForeignKey(Ranks, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='uploads/', null=True, blank=True)
    position = models.CharField(max_length=400, default='NONE', blank=True)

    def __str__(self):
        return 'Author - ' + self.rank.name + ' ' + self.name + ' - ' + str(self.id)


class Post(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title_file = models.FileField(upload_to='uploads/')
    docs_file = models.FileField(upload_to='uploads/')
    voiska = models.ForeignKey(Voiska1, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Post - ' + self.title + ' - ' + str(self.id)


class FileDoc(models.Model):
    file = models.FileField(upload_to='uploads/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.file:
            subprocess.Popen(['./soffice', '--headless', '--convert-to', 'pdf', '--outdir', '/Users/nidzhat/Documents/untitled4/media/uploads',self.file.path],cwd='/Applications/LibreOffice.app/Contents/MacOS')
            print('./soffice --headless --convert-to pdf --outdir ~/downloads {}'.format(self.file.path))
        super(FileDoc, self).save(*args, **kwargs)
