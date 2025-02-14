# Generated by Django 5.0 on 2024-12-07 08:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BagianAreaKerjaNakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TingkatPendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UnitKerjaNakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Kredensial',
            new_name='PermohonanKredensial',
        ),
        migrations.CreateModel(
            name='IdentitasNakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('nip_nps', models.CharField(max_length=30)),
                ('place_of_birth', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('mobile_phone', models.CharField(max_length=30)),
                ('no_ijazah', models.CharField(max_length=30)),
                ('no_str', models.CharField(max_length=30)),
                ('no_sip', models.CharField(max_length=30)),
                ('starting_work', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PendidikanPelatihanNakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tingkat_pendidikan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.tingkatpendidikan')),
            ],
        ),
    ]
