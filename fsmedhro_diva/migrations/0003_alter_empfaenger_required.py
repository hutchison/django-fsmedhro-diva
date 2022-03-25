# Generated by Django 3.2.12 on 2022-03-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsmedhro_diva', '0002_empfaenger_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empfaenger',
            name='required',
            field=models.BooleanField(help_text='DIVA-Mails werden immer an diesen Empfänger versandt. Nur die Pflichtempfänger erhalten personengebundene Daten für Rückfragen.', verbose_name='Pflichtversand'),
        ),
    ]