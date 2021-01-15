from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView

# def index(request):
#     return render(request, 'bank/index.html')
from bank.forms import RuttienForm, TransferMoney
from users.models import BankUser


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'bank/index.html'


def check_money(request):
    return render(request, 'bank/check_money.html')


def ruttien(request):
    form = RuttienForm(request.POST)
    if form.is_valid():
        try:
            money_rut = int(form.data.get('money'))
            username_current = request.user
            b = BankUser.objects.get(username=username_current)
            money_current = int(b.money)
            if money_rut <= money_current:
                money_current = money_current - money_rut
                b.money = str(money_current)
                b.save()
                # qs = BankUser.objects.filter(username=username_current)
                # BankUser.objects.get(username=username_current).money = money_current
                # BankUser.objects.get(username=username_current).save()
                return redirect('bank-home')
            else:
                messages.add_message(request,
                                     messages.SUCCESS,
                                     'Số tiền lớn hơn tài khoản')
            return redirect('ruttien')
        except:
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Định dạng không hợp lệ')
    return render(request, 'bank/ruttien.html', {'form': form})


def transfer_money(request):
    form = TransferMoney(request.POST)
    if form.is_valid():
        pass
    return render(request, 'bank/transfer_money.html', {'form': form})
