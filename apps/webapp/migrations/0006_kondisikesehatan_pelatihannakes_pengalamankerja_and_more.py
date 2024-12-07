# Generated by Django 5.0 on 2024-12-07 10:18

import apps.webapp.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_selfassesmensscore_selfassesmentscore'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KondisiKesehatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flg_tes_kesehatan', models.BooleanField()),
                ('tes_kesehatan', models.CharField(max_length=30)),
                ('flg_penyakit', models.BooleanField()),
                ('penyakit', models.CharField(max_length=30)),
                ('flg_pengobatan', models.BooleanField()),
                ('pengobatan', models.CharField(max_length=30)),
                ('flg_alergi', models.BooleanField()),
                ('alergi', models.CharField(max_length=30)),
                ('flg_perokok', models.BooleanField()),
                ('perokok', models.CharField(max_length=30)),
                ('flg_alkohol', models.BooleanField()),
                ('alkohol', models.CharField(max_length=30)),
                ('flg_operasi', models.BooleanField()),
                ('operasi', models.CharField(max_length=30)),
                ('flg_kecelakaan', models.BooleanField()),
                ('kecelakaan', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PelatihanNakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='N/A', max_length=100)),
                ('year', models.IntegerField(default=apps.webapp.models.current_year, validators=[django.core.validators.MinValueValidator(1984), apps.webapp.models.max_value_current_year])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PengalamanKerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institusi', models.CharField(default='N/A', max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('jabatan', models.CharField(max_length=30)),
                ('uraian_tugas', models.TextField()),
                ('alasan_berhenti', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='N/A', max_length=100)),
                ('profesi', models.CharField(max_length=30)),
                ('unit_kerja', models.CharField(max_length=30)),
                ('mobile_phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusPermohonan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='PendidikanPelatihanNakes',
            new_name='PendidikanNakes',
        ),
        migrations.DeleteModel(
            name='BagianAreaKerjaNakes',
        ),
        migrations.DeleteModel(
            name='UnitKerjaNakes',
        ),
        migrations.RenameField(
            model_name='permohonankredensial',
            old_name='first_name',
            new_name='unit_kerja',
        ),
        migrations.RemoveField(
            model_name='permohonankredensial',
            name='last_name',
        ),
        migrations.AddField(
            model_name='permohonankredensial',
            name='kepada',
            field=models.ManyToManyField(related_name='kepada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='permohonankredensial',
            name='rincian_kewenangan',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='permohonankredensial',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='selfassesmentnakes',
            name='permohonan_kredensial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.permohonankredensial'),
        ),
        migrations.AddField(
            model_name='kondisikesehatan',
            name='permohonan_kredensial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.permohonankredensial'),
        ),
        migrations.AddField(
            model_name='permohonankredensial',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.statuspermohonan'),
        ),
    ]