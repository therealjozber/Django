from django.db import models

# Create your models here.
class User(models.Model):#This is  a class that serves as a blueprint of creating objects
    #where as it inherits the  fromdjango class "models.Model" that give it  the properties like saving to the database
    age = models.IntegerField()#The age and name are the data of the created objects (attributes/properties of the class)
    name = models.CharField(max_length=100)


    def __str__(self):#this is the method /behavoir /actions of the class
        return self.name