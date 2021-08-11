from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
import datetime


class Bet(models.Model):

    Sports = [
        ('f', "football"),
        ('b', "basketball"),
        ('t', "tennis"),
    ]

    AllTypeBets = [
        ('football',
         (
             ('f_r', "Final Result"),
             ('g_o_u', "Goals over/under"),
             ('as_ha', "Asian Handicap"),
             ('t_ca', "Total Cards"),
             ('to_sc', "To Score"),
             ('as_g_o_u', "Asian Goals over/under"),
             ('to_r_y_c', "To Receive Yellow Card"),
             ('to_r_r_c', "To Receive Red Card"),
             ('to_r_c', "To Receive Card"),
             ('to_as_ca', "Total Asian Cards"),
             ('w_h', "Win Handicap"),
         ),
         ),
        ('basketball',
         (
             ('f_r', "Final Result"),
             ('h_to_h_p', "Head to Head Points"),
             ('pl_p', "Player Points"),
             ('t_p', "Total Points"),
             ('p_a', "Player Assists"),
             ('t_3_m', "Total 3pts made"),
             ('p_r', "Player Rebounds"),
             ('p_p_r', "Player Points/Rebounds"),
             ('t_s', "Top Scorer"),
             ('p_r_a', "Player Rebounds/Assists"),
             ('p_p_r_a', "Player Points/Rebounds/Assists"),
             ('mvp', "MVP"),
             ('d_d', "Double/Double"),
             ('w_h', "Win Handicap"),
         ),
         ),
        ('tennis',
         (
             ('f_r', "Final Result"),
             ('to_se', "Total Sets"),
             ('d_fa', "Double Faults"),
             ('to_ac', "Total aces"),
             ('pl_ac', "Player Aces"),
         ),
         ),
    ]

    Bookies = [
        ('bet365.png', "bet365"),
        ('stoiximan.png', "stoiximan"),
        ('opap.png', "opap"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sport = models.CharField(max_length=100, choices=Sports)
    type = models.CharField(max_length=100, choices=AllTypeBets)
    date_placed = models.DateTimeField(auto_now_add=True)
    match = models.CharField(max_length=200, default=' - ')
    pick = models.CharField(max_length=100, default='1')
    odds = models.FloatField()
    bookie = models.CharField(max_length=100, choices=Bookies, default='365', null= True)
    stake = models.FloatField(null= True)
    result = models.CharField(max_length=100, default=' - ')
    profit = models.FloatField(null= True)

    def __str__(self):
        return str(self.match)

    def last_month():
        items = Bet.objects.filter(date_placed__lte=datetime.datetime.today(),
                                   date_placed__gt=datetime.datetime.today() - datetime.timedelta(days=30))
        return items.aggregate(Sum('profit'))

    def last_3_months():
        items = Bet.objects.filter(date_placed__lte=datetime.datetime.today(),
                                   date_placed__gt=datetime.datetime.today() - datetime.timedelta(days=90))
        return items.aggregate(Sum('profit'))

    def longest_streak():
        items = Bet.objects.all()
        c = 0
        max = 0
        for item in items:
            if item.profit >= 0:
                c += 1
                if c > max:
                    max = c
            else:
                c = 0
        return max


