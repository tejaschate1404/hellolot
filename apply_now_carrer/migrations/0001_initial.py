# Generated by Django 5.0.6 on 2024-07-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('experience_years', models.PositiveIntegerField()),
                ('experience_months', models.PositiveIntegerField()),
                ('current_salary', models.PositiveIntegerField()),
                ('expected_salary', models.PositiveIntegerField()),
                ('available_to_join', models.PositiveIntegerField()),
                ('privacy_policy', models.BooleanField(default=False)),
            ],
        ),
    ]