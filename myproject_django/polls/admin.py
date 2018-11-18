from django.contrib import admin

from polls.models import *
# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_per_page=500
admin.site.register(Question)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Person)
admin.site.register(Classification)

