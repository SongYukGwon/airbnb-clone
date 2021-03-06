# Generated by Django 2.2.5 on 2021-05-03 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20210503_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenties'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'ordering': ['name'], 'verbose_name_plural': 'Room Types'},
        ),
        migrations.AlterModelOptions(
            name='rule',
            options={'verbose_name_plural': 'House Rules'},
        ),
        migrations.AlterField(
            model_name='room',
            name='amenity',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facility',
            field=models.ManyToManyField(blank=True, to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rule',
            field=models.ManyToManyField(blank=True, to='rooms.Rule'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.RoomType'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
