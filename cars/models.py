from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name="Vin", db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name="Color", max_length=64)
    brand = models.CharField(verbose_name="Brand", max_length=64)

    CAR_TYPES = (
        (1, "Седан"),
        (2, "Хэтчбэк"),
        (3, "Купе"),
        (4, "Универсал"),
        (5, "Минивэн"),
        (6, "Кроссовер"),
    )

    car_type = models.IntegerField(verbose_name="Car type", choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
