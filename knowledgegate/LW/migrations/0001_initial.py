# Generated by Django 4.2.3 on 2023-08-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LW.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='topic_images/')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LW.classes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LW.subject')),
            ],
        ),
    ]
