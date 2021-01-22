from users.models import BankUser
from django import forms


class RuttienForm(forms.Form):
    money = forms.CharField(label='Nhập số tiền cần rút', max_length=100)


class TransferMoney(forms.Form):
    bank_number = forms.CharField(label='Số tài khoản người nhận', )
    money = forms.CharField(label='Nhập số tiền cần chuyển', max_length=100)


class ChangePassForm(forms.Form):
    oldpassword = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'type': 'password', 'placeholder': 'Nhập mật khẩu cũ', 'class': 'span'}),
                                  error_messages={'required': 'Vui lòng không để trống trường này'})
    newpassword1 = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'type': 'password', 'placeholder': 'Mật khẩu mới', 'class': 'span'}),
                                   error_messages={'required': 'Vui lòng không để trống trường này'})
    newpassword2 = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'type': 'password', 'placeholder': 'Xác nhận mật khẩu mới', 'class': 'span'}),
                                   error_messages={'required': 'Vui lòng không để trống trường này'})

    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError(("Mật khẩu mới không trùng nhau."))
        return self.cleaned_data
