from django.contrib import admin

# Register your models here.
from ads.models import Company, Click, Ads, Campaign


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    pass


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    pass


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    pass




