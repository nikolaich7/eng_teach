# Generated by Django 4.0.3 on 2022-03-26 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picture_training', '0003_word_studied'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('words_repeat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_repeat', to='picture_training.word')),
                ('words_repeat_often', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_repeat_often', to='picture_training.word')),
                ('words_repeat_rare', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_repeat_rare', to='picture_training.word')),
                ('words_studied', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_studied', to='picture_training.word')),
                ('words_use', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_use', to='picture_training.word')),
            ],
        ),
    ]