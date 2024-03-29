# Generated by Django 2.2.4 on 2020-01-07 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pajsm', '0002_auto_20200107_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='paj',
            name='cadreref',
            field=models.FileField(blank=True, help_text="ATTENTION PAS D'ACCENT DANS LE NOM DU FICHIER", null=True, upload_to='DocsReferences', verbose_name='Cadre de référence ou document constitutif (qui encadre le fonctionnement du PAJ)'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titrecourt', models.CharField(max_length=200, verbose_name='Non court et évocateur du document')),
                ('documentation', models.FileField(help_text="ATTENTION PAS D'ACCENT DANS LE NOM DES FICHIERS", upload_to='DocsReferences', verbose_name='Documents pertinants')),
                ('tribunal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pajsm.Paj')),
            ],
        ),
    ]
