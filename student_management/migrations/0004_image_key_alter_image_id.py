# Generated by Django 4.0.2 on 2022-02-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0003_remove_image_key_alter_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='key',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
