from django.contrib import admin
from .models import ComputerScore,PlayerScore, User,RPSModel

# Register your models here.
admin.site.register(User)
admin.site.register(PlayerScore)
admin.site.register(ComputerScore)
admin.site.register(RPSModel)
