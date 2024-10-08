# Generated by Django 4.2.16 on 2024-09-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_step_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='custom_description',
        ),
        migrations.AddField(
            model_name='step',
            name='path',
            field=models.CharField(blank=True, choices=[('Adjust', 'Adjust'), ('Collaborate', 'Collaborate'), ('Execute', 'Execute'), ('Plan', 'Plan'), ('Practice', 'Practice'), ('Reflect', 'Reflect'), ('Research', 'Research'), ('Start', 'Start'), ('Review', 'Review'), ('Workout', 'Workout')], max_length=255),
        ),
        migrations.AlterField(
            model_name='step',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
