# Generated by Django 4.0.10 on 2023-11-01 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('class_type', models.CharField(choices=[('EP', 'EP'), ('P', 'P')], max_length=2)),
                ('level', models.CharField(max_length=1)),
                ('sub_level', models.CharField(max_length=1)),
                ('dept', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('month', models.CharField(choices=[('01', 'ม.ค.'), ('02', 'ก.พ.'), ('03', 'มี.ค.'), ('04', 'เม.ย.'), ('05', 'พ.ค.'), ('06', 'มิ.ย.'), ('07', 'ก.ค.'), ('08', 'ส.ค.'), ('09', 'ก.ย.'), ('10', 'ต.ค.'), ('11', 'พิ.ย.'), ('12', 'ธ.ค.')], max_length=10)),
                ('year', models.CharField(default='2023', max_length=4)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]