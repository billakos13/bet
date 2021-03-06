# Generated by Django 3.2.5 on 2021-08-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('f', 'football'), ('b', 'basketball'), ('t', 'tennis')], max_length=100)),
                ('type', models.CharField(choices=[('f', (('f_r', 'Final Result'), ('g_o_u', 'Goals over/under'), ('as_ha', 'Asian Handicap'), ('t_ca', 'Total Cards'), ('to_sc', 'To Score'), ('as_g_o_u', 'Asian Goals over/under'), ('to_r_y_c', 'To Receive Yellow Card'), ('to_r_r_c', 'To Receive Red Card'), ('to_r_c', 'To Receive Card'), ('to_as_ca', 'Total Asian Cards'), ('w_h', 'Win Handicap'))), ('b', (('f_r', 'Final Result'), ('h_to_h_p', 'Head to Head Points'), ('pl_p', 'Player Points'), ('t_p', 'Total Points'), ('p_a', 'Player Assists'), ('t_3_m', 'Total 3pts made'), ('p_r', 'Player Rebounds'), ('p_p_r', 'Player Points/Rebounds'), ('t_s', 'Top Scorer'), ('p_r_a', 'Player Rebounds/Assists'), ('p_p_r_a', 'Player Points/Rebounds/Assists'), ('mvp', 'MVP'), ('d_d', 'Double/Double'), ('w_h', 'Win Handicap'))), ('t', (('f_r', 'Final Result'), ('to_se', 'Total Sets'), ('d_fa', 'Double Faults'), ('to_ac', 'Total aces'), ('pl_ac', 'Player Aces')))], max_length=100)),
                ('date_placed', models.DateTimeField(auto_now_add=True)),
                ('match', models.CharField(default=' - ', max_length=200)),
                ('pick', models.CharField(default='1', max_length=100)),
                ('odds', models.FloatField()),
                ('bookie', models.CharField(choices=[('365', 'bet365'), ('st', 'stoiximan'), ('o', 'opap')], default='365', max_length=100, null=True)),
                ('stake', models.FloatField(null=True)),
                ('result', models.CharField(default=' - ', max_length=100)),
                ('profit', models.FloatField(null=True)),
            ],
        ),
    ]
