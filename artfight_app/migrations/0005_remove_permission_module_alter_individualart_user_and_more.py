# Generated by Django 4.2 on 2024-04-22 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artfight_app', '0004_remove_duel_art_duel_artone_duel_arttwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='module',
        ),
        migrations.AlterField(
            model_name='individualart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
