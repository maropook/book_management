# Generated by Django 3.2.6 on 2021-09-09 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('title_kana', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('author_kana', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=250)),
                ('sales_date', models.CharField(max_length=250)),
            ],
        ),
    ]
