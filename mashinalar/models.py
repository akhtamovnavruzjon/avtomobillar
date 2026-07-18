from django.db import models

class Cars(models.Model):
    name=models.CharField(max_length=50)
    year=models.IntegerField()
    color=models.CharField(max_length=25)
    image=models.ImageField(upload_to='cover')
    price=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return self.name
