# Generated by Django 4.0.3 on 2022-03-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0005_alter_artical_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='slug',
            field=models.CharField(default=0, max_length=130),
        ),
    ]