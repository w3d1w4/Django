from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(null=False)
    def to_Dict(self):
        return {'name':self.name, 'price':self.price,}
