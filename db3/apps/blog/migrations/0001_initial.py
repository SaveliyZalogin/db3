# Generated by Django 3.0.3 on 2020-02-28 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('ava', models.ImageField(blank=True, upload_to='static/images')),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Key_word',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('key_word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=100)),
                ('post_annotation', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('post_image', models.ImageField(blank=True, upload_to='static/images', verbose_name='photo')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('key_words', models.ManyToManyField(blank=True, to='blog.Key_word')),
            ],
        ),
    ]
