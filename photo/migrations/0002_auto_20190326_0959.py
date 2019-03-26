# Generated by Django 2.1.7 on 2019-03-26 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['comment_post', 'author', 'commented_image']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='imageuploader_profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_avatar',
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Comments'),
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='photo.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_post',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='tag_someone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]