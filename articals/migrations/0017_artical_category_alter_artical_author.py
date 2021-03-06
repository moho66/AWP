# Generated by Django 4.0.3 on 2022-03-12 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articals', '0016_alter_artical_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='category',
            field=models.CharField(default='code', max_length=50),
        ),
        migrations.AlterField(
            model_name='artical',
            name='author',
            field=models.ForeignKey(default='username', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
