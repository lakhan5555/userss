# Generated by Django 3.1.3 on 2021-03-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=100, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
