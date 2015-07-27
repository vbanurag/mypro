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



class user_reg_admin(admin.ModelAdmin):
	list_display=['get_name','get_uname','course_name']

	def get_name(self, obj):                                        # list display in foregin key concept
		return obj.user.first_name
	def get_uname(self, obj):
		return obj.user.username
	get_name.admin_order_field  = 'user'  #Allows column order sorting
	get_name.short_description = 'first_name'  #Renames column head
	get_uname.admin_order_field  = 'user'  #Allows column order sorting
	get_uname.short_description = 'username'  #Renames column head



admin.site.register(students)
admin.site.register(lang)
admin.site.register(writ)
admin.site.register(stu)
admin.site.register(Accounts)
admin.site.register(Enquiry,Enquiry_admin)
admin.site.register(feedback,feedback_admin)
admin.site.register(user_reg, user_reg_admin)
