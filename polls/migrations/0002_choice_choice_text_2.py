# Generated by Django 3.2.6 on 2021-08-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text_2',
            field=models.CharField(default=0, max_length=200),
        ),
    ]