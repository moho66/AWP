# Generated by Django 4.0.3 on 2022-03-13 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0019_alter_artical_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articals.category'),
        ),
    ]