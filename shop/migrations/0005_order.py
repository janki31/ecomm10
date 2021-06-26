# Generated by Django 3.1.2 on 2021-06-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('itemjson', models.CharField(max_length=5000)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(default='', max_length=25)),
                ('email', models.EmailField(default='', max_length=50)),
                ('address1', models.CharField(default='', max_length=50)),
                ('address2', models.CharField(default='', max_length=50)),
                ('mobileno', models.IntegerField(default=0)),
                ('state', models.CharField(default=0, max_length=10)),
                ('zipcode', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
    ]