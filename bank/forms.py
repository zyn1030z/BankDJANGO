from users.models import BankUser
from django import forms


class RuttienForm(forms.Form):
    money = forms.CharField(label='Nhập số tiền cần rút', max_length=100)


class TransferMoney(forms.Form):
    bank_number = forms.CharField(label='Số tài khoản người nhận',)
    money = forms.CharField(label='Nhập số tiền cần chuyển', max_length=100)

