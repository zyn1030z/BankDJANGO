from django.urls import path

from bank import views
# from bank.views import IndexView
from bank.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='bank-home'),
    path('check_money/', views.check_money, name='check_money'),
    path('ruttien/', views.Withdrawal, name='ruttien'),
    path('transfer_money/', views.transfer_money, name='transfer_money'),
    path('change_pass/', views.change_pass, name='change_pass')
]
