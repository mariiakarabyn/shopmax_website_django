from django.db import models
from . abstract_models import Subscribable


class Subscribe(Subscribable):
    
    def __str__(self):
        return self.email
    

class Contact(Subscribable):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    