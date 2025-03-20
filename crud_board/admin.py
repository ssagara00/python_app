from django.contrib import admin

from crud_board.models import HouseEstimate, User

# Register your models here.
admin.site.register(User)
admin.site.register(HouseEstimate)
