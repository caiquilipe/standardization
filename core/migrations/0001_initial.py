# Generated by Django 4.1.7 on 2023-02-28 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WalletModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.IntegerField(choices=[(0, 'Bonus'), (1, 'Real')])),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('wallet', models.OneToOneField(limit_choices_to={'type': 1}, on_delete=django.db.models.deletion.PROTECT, to='core.walletmodel')),
            ],
        ),
    ]
