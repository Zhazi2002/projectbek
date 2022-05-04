# Generated by Django 4.0.2 on 2022-02-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_posts_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
