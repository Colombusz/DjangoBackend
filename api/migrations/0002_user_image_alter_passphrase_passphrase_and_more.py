# Generated by Django 5.1.3 on 2024-11-17 04:13

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile/default.jpg', null=True, upload_to=api.models.upload_to_profile, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='passphrase',
            name='passphrase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.role'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('url', models.CharField(default='example.com', max_length=255)),
                ('image', models.ImageField(blank=True, default='account/default.jpg', null=True, upload_to=api.models.upload_to_account, verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to='api.account')),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entropy', models.FloatField(blank=True, null=True)),
                ('estimated_cracking_time', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(max_length=255)),
                ('password', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to='api.password')),
            ],
        ),
    ]