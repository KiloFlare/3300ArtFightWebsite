# Generated by Django 4.2 on 2024-04-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artfight_app', '0002_module_permission_role_alter_individualart_artpiece_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('art', models.ManyToManyField(to='artfight_app.individualart')),
            ],
        ),
    ]
