from django.db import models
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    village = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contract(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    crop = models.CharField(max_length=100)
    quantity = models.FloatField()
    price = models.FloatField()
    contract_date = models.DateField()
    delivery_status = models.CharField(max_length=20, default='Pending')
    payment_status = models.CharField(max_length=20, default='Pending')
    def __str__(self):
        return f"{self.farmer.name} - {self.buyer.name}"


# Create your models here.
