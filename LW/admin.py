from django.contrib import admin
from .models import Classes, Subject, Topic,FAQ, About
# Register your models here.

admin.site.register(Classes)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(FAQ)
admin.site.register(About)

