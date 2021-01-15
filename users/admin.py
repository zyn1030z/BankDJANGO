from django.contrib import admin

# Register your models here.
from users.models import BankUser

admin.site.register(BankUser)
