# Generated by Django 2.2.5 on 2019-09-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('data', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tool',
        ),
    ]