import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class ProfesiNakes(models.Model):
    name = models.CharField(max_length=200)


class IdentitasNakes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    nip_nps = models.CharField(max_length=30)
    place_of_birth = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    address = models.TextField()
    mobile_phone = models.CharField(max_length=30)
    no_ijazah = models.CharField(max_length=30)
    no_str = models.CharField(max_length=30)
    no_sip = models.CharField(max_length=30)
    starting_work = models.DateField(
        validators=[MinValueValidator(1984), max_value_current_year],
        default=current_year,
    )


class TingkatPendidikan(models.Model):
    name = models.CharField(max_length=30)


class PendidikanNakes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tingkat_pendidikan = models.ForeignKey(TingkatPendidikan, on_delete=models.CASCADE)
    profesi = models.CharField(max_length=30, default="N/A")
    institusi = models.CharField(max_length=100, default="N/A")
    jurusan = models.CharField(max_length=30, default="N/A")
    graduation_year = models.IntegerField(
        validators=[MinValueValidator(1984), max_value_current_year],
        default=current_year,
    )


class PelatihanNakes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, default="N/A")
    year = models.IntegerField(
        validators=[MinValueValidator(1984), max_value_current_year],
        default=current_year,
    )


class Referensi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100, default="N/A")
    profesi = models.CharField(max_length=30)
    unit_kerja = models.CharField(max_length=30)
    mobile_phone = models.CharField(max_length=30)
    email = models.EmailField()


class PengalamanKerja(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institusi = models.CharField(max_length=100, default="N/A")
    start_date = models.DateField()
    end_date = models.DateField()
    jabatan = models.CharField(max_length=30)
    uraian_tugas = models.TextField()
    alasan_berhenti = models.TextField()


class SelfAssesmentScore(models.Model):
    description = models.CharField(max_length=100)


class StatusPermohonan(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PermohonanKredensial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(StatusPermohonan, on_delete=models.CASCADE, default=1)
    rincian_kewenangan = models.CharField(max_length=100, default="N/A")
    unit_kerja = models.CharField(max_length=30)
    kepada = models.ManyToManyField(User, related_name="kepada")


class SelfAssesmentNakes(models.Model):
    permohonan_kredensial = models.ForeignKey(
        PermohonanKredensial, on_delete=models.CASCADE, default=None
    )
    rincian_kewenangan = models.TextField()
    score = models.ForeignKey(SelfAssesmentScore, on_delete=models.CASCADE)


class KondisiKesehatan(models.Model):
    permohonan_kredensial = models.ForeignKey(
        PermohonanKredensial, on_delete=models.CASCADE
    )
    flg_tes_kesehatan = models.BooleanField()
    tes_kesehatan = models.CharField(max_length=30)
    flg_penyakit = models.BooleanField()
    penyakit = models.CharField(max_length=30)
    flg_pengobatan = models.BooleanField()
    pengobatan = models.CharField(max_length=30)
    flg_alergi = models.BooleanField()
    alergi = models.CharField(max_length=30)
    flg_perokok = models.BooleanField()
    perokok = models.CharField(max_length=30)
    flg_alkohol = models.BooleanField()
    alkohol = models.CharField(max_length=30)
    flg_operasi = models.BooleanField()
    operasi = models.CharField(max_length=30)
    flg_kecelakaan = models.BooleanField()
    kecelakaan = models.CharField(max_length=30)
