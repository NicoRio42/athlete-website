from django.contrib import admin

from .models import HeadBanner, HeadText, Article, SponsorBanner, Sponsor

admin.site.register(HeadBanner)
admin.site.register(HeadText)
admin.site.register(Article)
admin.site.register(SponsorBanner)
admin.site.register(Sponsor)