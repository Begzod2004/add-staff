from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=50)


    def __str__(self):
        return self.gender



class Staff(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.first_name