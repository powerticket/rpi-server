# Generated by Django 3.1.1 on 2020-09-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200930_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.answer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.question'),
        ),
    ]