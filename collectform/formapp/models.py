from django.db import models

# Create your models here.

# * Foreignkey was not used.
GENDER  = (
    ('M', 'M'),
    ('F', 'F')
)


CLASS  = (
     ('JSS 1', 'JSS 1'),
     ('JSS 2', 'JSS 2'),
     ('JSS 3', 'JSS 3'),
     ('SSS 1', 'SSS 1'),
     ('SSS 2', 'SSS 2'),
     ('SSS 3', 'SSS 3')
)


class Candidate(models.Model):
    name       = models.CharField(max_length=80)
    phone      = models.CharField(max_length=30)
    email      = models.CharField(max_length=120)
    gender     = models.CharField(max_length=1,null=True, choices=GENDER)
    career     = models.CharField(max_length=80, null=True, choices=CLASS)
    
    
    
    def __str__(self):
        return self.name