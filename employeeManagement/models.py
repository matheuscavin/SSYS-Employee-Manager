from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    department = models.CharField(max_length=40)

    def __str__(self):
        return self.name
