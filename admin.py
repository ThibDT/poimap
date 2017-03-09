from django.contrib import admin
from django.contrib.gis import admin
from models import Hostings, HostingType, PaymentType, OpeningDate, Contact, SleepingType, Sleeping

# Register your models here.

class SleepingInlineAdmin(admin.TabularInline):
    model = Sleeping
    extra = 1

class ContactInlineAdmin(admin.TabularInline):
    model = Contact
    extra = 1

class HostingsAdmin(admin.GeoModelAdmin):
    list_display = ['name','zipcode','city']
    inlines = (SleepingInlineAdmin, ContactInlineAdmin)

admin.site.register(Hostings, HostingsAdmin)
admin.site.register(HostingType)
admin.site.register(PaymentType)
admin.site.register(OpeningDate)
admin.site.register(Contact)
admin.site.register(SleepingType)
admin.site.register(Sleeping)
