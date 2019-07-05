from django.db import models

# Create your models here.
class Registration(models.Model):
    groupname=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    account=models.DecimalField(max_digits=16,decimal_places=0)
    mobile=models.DecimalField(max_digits=10,decimal_places=0)
    passwoord=models.CharField(max_length=15)

    def __str__(self):
        return 'group:%s  name:%s'% (self.groupname,self.name)

