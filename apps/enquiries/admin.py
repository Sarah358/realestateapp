from django.contrib import admin

from .models import Enquiry


# Register your models here.
class EnquiyAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone_number","message"]

admin.site.register(Enquiry,EnquiyAdmin)
