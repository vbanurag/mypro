from django.contrib import admin
from django.db import models
from day_12.models import lang
from day_12.models import stu
from day_12.models import writ
from day_12.models import students
from day_12.models import *


class Enquiry_admin(admin.ModelAdmin):
	list_display=['name','email','phone','is_active']
	search_fields=['name','email']

class feedback_admin(admin.ModelAdmin):
	list_display=['course','idea']


admin.site.register(students)
admin.site.register(lang)
admin.site.register(writ)
admin.site.register(stu)
admin.site.register(Accounts)
admin.site.register(Enquiry,Enquiry_admin)
admin.site.register(feedback,feedback_admin)
admin.site.register(user_reg)
