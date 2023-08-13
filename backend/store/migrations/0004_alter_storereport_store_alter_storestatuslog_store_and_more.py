# Generated by Django 4.2.4 on 2023-08-12 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_storeStatusLog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereport',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='store.store'),
        ),
        migrations.AlterField(
            model_name='storestatuslog',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_logs', to='store.store'),
        ),
        migrations.AlterField(
            model_name='storetiming',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='store.store'),
        ),
    ]