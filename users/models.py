from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    uid = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, default="")
    password = models.CharField(max_length=30, default="")
    address = models.TextField(max_length=255, default="")
    pincode = models.IntegerField(default=000000)