from django.contrib import admin

# Register your models here.
from app.models import *

class WebpageView(admin.ModelAdmin):
    list_display=['topic_name','name','url']

admin.site.register(Topic)
admin.site.register(Webpage,WebpageView)
admin.site.register(Access_Records)