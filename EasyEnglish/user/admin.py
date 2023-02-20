from django.contrib import admin
from .models import Learnt, Ranking

# Register your models here.
admin.site.register(Ranking)
admin.site.register(Learnt)