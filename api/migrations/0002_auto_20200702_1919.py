# Generated by Django 3.0.5 on 2020-07-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.DO_NOTHING, related_name='title_category', to='api.Categories'),
            preserve_default=False,
        ),
    ]
