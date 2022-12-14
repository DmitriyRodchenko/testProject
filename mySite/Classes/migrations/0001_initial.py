# Generated by Django 4.1.1 on 2022-09-27 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=200, verbose_name='Class name')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fam', models.CharField(max_length=200, verbose_name='Last Name')),
                ('student_im', models.CharField(max_length=200, verbose_name='First Name')),
                ('student_otch', models.CharField(max_length=200, verbose_name='Second name')),
                ('student_birthd', models.DateTimeField(verbose_name='birth date')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.studentclass')),
            ],
        ),
    ]
