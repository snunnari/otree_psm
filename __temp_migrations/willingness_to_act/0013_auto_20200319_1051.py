# Generated by Django 2.2.4 on 2020-03-19 09:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('willingness_to_act', '0012_auto_20200319_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='donate_cause',
        ),
        migrations.AddField(
            model_name='player',
            name='donate_',
            field=otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n        How willing are you to give to good causes without expecting anything in return?\n        '),
        ),
    ]
