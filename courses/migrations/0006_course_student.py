# Generated by Django 2.2.2 on 2019-06-06 13:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_auto_20190606_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
    ]
