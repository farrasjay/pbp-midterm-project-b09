# Generated by Django 4.1 on 2022-10-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uhealths', '0003_commentketiga'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentketiga',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]
