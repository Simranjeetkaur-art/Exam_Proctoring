# Generated by Django 4.2.2 on 2023-06-17 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'exam_attempt',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExamSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_attempt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.examattempt')),
            ],
            options={
                'db_table': 'exam_submission',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_option', models.CharField(max_length=100)),
                ('exam_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.examsubmission')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
            options={
                'db_table': 'student_answer',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='examsubmission',
            name='student_answers',
            field=models.ManyToManyField(through='quiz.StudentAnswer', to='quiz.question'),
        ),
    ]