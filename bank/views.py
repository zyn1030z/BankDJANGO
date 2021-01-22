from django.contrib import messages, auth
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView

from bank.forms import RuttienForm, TransferMoney, ChangePassForm
from users.models import BankUser


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'bank/index.html'


def check_money(request):
    return render(request, 'bank/check_money.html')


def Withdrawal(request):
    if request.method == "POST":
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
                    messages.add_message(request,
                                         messages.SUCCESS,
                                         'Rút tiền thành công')
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
    form = RuttienForm()
    return render(request, 'bank/ruttien.html', {'form': form})


def transfer_money(request):
    if request.method == "POST":
        form = TransferMoney(request.POST)
        if form.is_valid():
            try:
                username_current = request.user
                money_send = int(form.data.get('money'))
                bank_number_receiver = form.data.get('bank_number')
                user_send = BankUser.objects.get(username=username_current)
                user_receiver = BankUser.objects.get(bank_number=bank_number_receiver)
                money_current = int(user_send.money)
                if money_send < money_current:
                    money_current = money_current - money_send
                    user_send.money = str(money_current)
                    user_send.save()
                    user_receiver.money = str(int(user_receiver.money) + money_send)
                    user_receiver.save()
                    messages.add_message(request,
                                         messages.SUCCESS,
                                         'Chuyển tiền thành công')
                    return redirect('bank-home')
            except:
                messages.add_message(request,
                                     messages.SUCCESS,
                                     'Định dạng không hợp lệ')
    form = TransferMoney()
    return render(request, 'bank/transfer_money.html', {'form': form})


def change_pass(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            newpassword = form.cleaned_data['newpassword1'],
            username = request.user.username
            password_check = form.data.get('oldpassword')
            user = BankUser.objects.get(username=username)
            print(newpassword)
            # if user.check_password('a'):
            #     user.set_password('1')
            #     user.save()
            #     redirect('logout')
            # messages.add_message(request,
            #                      messages.SUCCESS,
            #                      'Mật khẩu không đúng')
            #

    # if user is not None:
    #     user.set_password(newpassword)
    #     user.save()
    #     return redirect('bank-home')

    # else:
    #     messages.add_message(request,
    #                          messages.SUCCESS,
    #                          'Mật khẩu không đúng')
    #     return render(request, 'bank/change_pass.html',
    #                   {'form': form})

    form = ChangePassForm()
    # form = PasswordChangeForm(request.user)
    return render(request, 'bank/change_pass.html', {'form': form})
