# Generated by Django 5.0.6 on 2024-08-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.womantowomanmentoring.org/wp-content/uploads/placeholder.jpg', max_length=500),
        ),
    ]
