# Generated by Django 5.1.3 on 2024-12-02 13:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_picture',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recruiter', to=settings.AUTH_USER_MODEL),
        ),
    ]
