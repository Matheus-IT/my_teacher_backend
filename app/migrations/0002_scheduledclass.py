# Generated by Django 4.0.6 on 2022-10-11 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_classes', to='app.teacher')),
            ],
        ),
    ]
