# Generated by Django 3.1.3 on 2020-11-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0002_auto_20201109_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='price',
        ),
    ]
