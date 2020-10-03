from django.contrib import admin
from .models import Member, Community, TempMember
# Register your models here.

admin.site.register(Member)
admin.site.register(Community)
admin.site.register(TempMember)