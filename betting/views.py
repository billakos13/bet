from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Bet
from .forms import BetForm
from django.db.models import Sum



def index(request):
    all_bets = Bet.objects.all().order_by('id')
    total_bets = Bet.objects.count()
    won_bets = Bet.objects.filter(profit__gt=0).count()
    lost_bets = Bet.objects.filter(profit__lt=0).count()
    pushed_bets = total_bets - won_bets - lost_bets
    total_stake = Bet.objects.aggregate(Sum('stake'))['stake__sum']
    total_returns = Bet.objects.aggregate(Sum('profit'))['profit__sum']
    bank = total_returns - total_stake
    yields = ((total_returns - total_stake)/total_stake)*100
    last_month_profit = Bet.last_month()['profit__sum']
    last_3_months_profit = Bet.last_3_months()['profit__sum']
    longest_streak = Bet.longest_streak()

    paginator = Paginator(all_bets, 15)

    page_number = request.GET.get('page')
    bets = paginator.get_page(page_number)

    context = {
        'bets':bets,
        'total_bets':total_bets,
        'won_bets':won_bets,
        'pushed_bets':pushed_bets,
        'lost_bets':lost_bets,
        'total_stake':total_stake,
        'total_returns':total_returns,
        'yields':yields,
        'bank':bank,
        'last_month_profit':last_month_profit,
        'last_3_months_profit':last_3_months_profit,
        'longest_streak':longest_streak,
    }
    return render(request, 'index.html', context)


def create_bet(request):
    form = BetForm()
    if request.method == "POST":
        form = BetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'create-bet.html', context)


def update_bet(request, pk):
    bet = Bet.objects.get(id=pk)
    x = BetForm(instance=bet)
    if request.method == "POST":
        x = BetForm(request.POST, instance=bet)
        if x.is_valid():
            x.save()
            return redirect('/')
    context = {'x':x}
    return render(request, 'update-bet.html', context)


def delete_bet(request, pk):
    bet = Bet.objects.get(id=pk)
    if request.method == "POST":
        bet.delete()
        return redirect('/')
    context = {'bet':bet}
    return render(request, 'delete-bet.html', context)




