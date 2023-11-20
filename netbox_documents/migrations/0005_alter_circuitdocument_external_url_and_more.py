# Generated by Django 4.2.7 on 2023-11-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_documents', '0004_locationdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuitdocument',
            name='external_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='devicedocument',
            name='external_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='devicetypedocument',
            name='external_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='locationdocument',
            name='external_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sitedocument',
            name='external_url',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
