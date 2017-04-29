from django.db import models
from django.contrib.auth.models import User

class BuyerAccount(models.Model):
    name = models.CharField(max_length=999)
    account_id = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserSetting(models.Model):
    user = models.ForeignKey(User, related_name='setting_user')
    buyer_account = models.ForeignKey(BuyerAccount, related_name='account_buyer')

    def __str__(self):
        return str(self.user) + '\'s Settings'
# Create your models here.
