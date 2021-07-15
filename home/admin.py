from django.contrib import admin
from .models import App, CustomText, Subscription

admin.site.register(CustomText)
admin.site.register(App)
admin.site.register(Subscription)

# Register your models here.
