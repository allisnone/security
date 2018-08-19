from django.db import models

# Create your models here.
class chkportinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    IPs = models.CharField(max_length=50)
    ports=models.CharField(max_length=10)
    contact = models.CharField(max_length=50)
    