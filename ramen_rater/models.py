from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator


class Ramen(models.Model):
    STYLE_CHOICES = [
        ('bar', 'Bar'),
        ('cup', 'Cup'),
        ('box', 'Box'),
        ('bowl', 'Bowl'),
        ('can', 'Can'),
        ('tray', 'Tray'),
        ('pack', 'Pack'),

    ]
    brand = models.CharField(max_length=100) 
    variety = models.CharField(max_length=100)
    style = models.CharField(max_length=7, choices=STYLE_CHOICES)
    country = models.CharField(max_length=70)
    daterate = models.DateTimeField(default=timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    blank=True)
    stars = models.FloatField(validators=[MinValueValidator(0), 
                              MaxValueValidator(10)])

    def __str__(self):
        return self.brand
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def was_rated_recently(self):
        return self.daterate >= timezone.now() - datetime.timedelta(days=1)



    
     