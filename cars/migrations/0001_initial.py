# Generated by Django 2.2.1 on 2019-05-21 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Vin')),
                ('color', models.CharField(max_length=64, verbose_name='Color')),
                ('brand', models.CharField(max_length=64, verbose_name='Brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэтчбэк'), (3, 'Купе'), (4, 'Универсал'), (5, 'Минивэн'), (6, 'Кроссовер')], verbose_name='Car type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
