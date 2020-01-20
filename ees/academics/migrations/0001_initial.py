# Generated by Django 3.0.2 on 2020-01-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAcademics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_terms', models.TextField(default='')),
                ('school_pdf_calender', models.FileField(upload_to='schoolacademiccalenderpdf/')),
                ('awards_scholarships', models.TextField(default='')),
                ('disciplinary_rules', models.TextField(default='')),
                ('examination_promotion', models.TextField(default='')),
                ('leave_of_absence', models.TextField(default='')),
                ('certificate', models.TextField(default='')),
                ('notes_parents_guardians', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'AboutAcademics',
                'verbose_name_plural': 'AboutAcademics',
            },
        ),
        migrations.CreateModel(
            name='HigherSecondarySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_hs', models.TextField(default='')),
                ('courses_study', models.TextField(default='')),
                ('school_uniform', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'HigherSecondarySchool',
                'verbose_name_plural': 'HigherSecondarySchool',
            },
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_school', models.TextField(default='')),
                ('coscholastic_activities', models.TextField(default='')),
                ('cocurricular_activities', models.TextField(default='')),
                ('work_experience', models.TextField(default='')),
                ('school_uniform', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'HighSchool',
                'verbose_name_plural': 'HighSchool',
            },
        ),
        migrations.CreateModel(
            name='SchoolAnthem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_anthem', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'SchoolAnthem',
                'verbose_name_plural': 'SchoolAnthem',
            },
        ),
        migrations.CreateModel(
            name='SchoolTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_timing', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'SchoolTiming',
                'verbose_name_plural': 'SchoolTiming',
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_header', models.TextField(default='')),
                ('syllabus_pdf', models.FileField(upload_to='syllabuspdf/')),
            ],
            options={
                'verbose_name': 'Syllabus',
                'verbose_name_plural': 'Syllabus',
            },
        ),
    ]
