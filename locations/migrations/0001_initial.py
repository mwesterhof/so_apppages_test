# Generated by Django 3.0.8 on 2020-07-30 09:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail_app_pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
                'ordering': ['feature'],
            },
        ),
        migrations.CreateModel(
            name='LocationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Locations List',
                'verbose_name_plural': 'Locations Lists',
            },
            bases=(wagtail_app_pages.models.AppPageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=60, null=True)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(choices=[('a', 'A'), ('b', 'B')], max_length=2, null=True)),
                ('zipcode', models.CharField(max_length=5, null=True)),
                ('lat', models.CharField(max_length=50, null=True)),
                ('lon', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=40, null=True)),
                ('places_id', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=100, null=True)),
                ('google_url', models.CharField(blank=True, max_length=100, null=True)),
                ('entity', models.CharField(blank=True, max_length=10, null=True)),
                ('truck_url', models.CharField(blank=True, max_length=100, null=True)),
                ('trailer_url', models.CharField(blank=True, max_length=100, null=True)),
                ('supplies_url', models.CharField(blank=True, max_length=100, null=True)),
                ('features', models.ManyToManyField(to='locations.Feature')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'ordering': ['name'],
            },
        ),
    ]
