from django.db import models

# Create your models here.
class Supplier(models.Model):
    cateogry=models.CharField(max_length=15)
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    manufacture_date=models.DateField()
    expiry_date=models.DateField(null=True,blank=True)
    mrp=models.IntegerField(default=0)


    def __str__(self):
        return self.name