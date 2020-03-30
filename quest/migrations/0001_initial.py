# Generated by Django 3.0.3 on 2020-03-30 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('goal', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('badge', models.CharField(max_length=300, null=True)),
                ('reward', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quest.Category')),
            ],
            options={
                'db_table': 'quests',
            },
        ),
        migrations.CreateModel(
            name='UserQuestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_achieved', models.BooleanField(null=True)),
                ('is_claimed', models.BooleanField(null=True)),
                ('is_rewarded', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quest.Quest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'user_quest_histories',
            },
        ),
        migrations.AddField(
            model_name='quest',
            name='user',
            field=models.ManyToManyField(null=True, through='quest.UserQuestHistory', to='user.User'),
        ),
    ]
