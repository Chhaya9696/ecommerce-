# Generated by Django 3.0.5 on 2024-05-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20240428_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]