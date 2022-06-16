# Generated by Django 4.0.5 on 2022-06-15 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('left_title', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('right_title', models.CharField(blank=True, max_length=255, null=True)),
                ('opening', models.TextField(blank=True, max_length=255, null=True)),
                ('closing', models.TextField(blank=True, max_length=255, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=255, null=True)),
                ('domain_text', models.TextField(blank=True, max_length=255, null=True)),
                ('designer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('designer_url', models.URLField(blank=True, max_length=255, null=True)),
                ('related_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
