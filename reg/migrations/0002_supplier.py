# Generated by Django 2.2.3 on 2019-07-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateogry', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('manufacture_date', models.DateField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('mrp', models.IntegerField(default=0)),
            ],
        ),
    ]
