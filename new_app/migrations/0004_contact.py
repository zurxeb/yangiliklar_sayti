# Generated by Django 4.0 on 2024-04-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_alter_news_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]