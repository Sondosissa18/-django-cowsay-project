from django.db import models

import subprocess

class Cowtext(models.Model):
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.text}"
