from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class PinCode(models.Model):
    number = models.CharField(max_length=50, validators=[RegexValidator(regex='\w+')],unique=True)

    def __str__(self):
        return 'Pin - ' + str(self.number)
