from django.contrib import admin

from .models import ZMK, RTC, RTCObject

admin.site.register(ZMK)
admin.site.register(RTC)
admin.site.register(RTCObject)
