# Generated by Django 3.1.2 on 2021-05-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(default='', max_length=200)),
                ('category', models.CharField(default='', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]