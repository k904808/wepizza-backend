# Generated by Django 3.0.3 on 2020-03-24 17:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('offer', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rewards',
            },
        ),
        migrations.CreateModel(
            name='RewardHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_rewarded', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Reward')),
            ],
            options={
                'db_table': 'reward_histories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=500, null=True)),
                ('is_activated', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Grade')),
                ('reward', models.ManyToManyField(null=True, through='user.RewardHistory', to='user.Reward')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Store')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='rewardhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'feedbacks',
            },
        ),
    ]
