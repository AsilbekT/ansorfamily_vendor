# Generated by Django 4.0.6 on 2022-09-04 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_order_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(auto_now_add=True),
        ),
    ]
