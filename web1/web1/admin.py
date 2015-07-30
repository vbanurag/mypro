from django.contrib import admin
from django.db import models
from web1.models import *


class Enquiry_admin(admin.ModelAdmin):
	list_display=['name','email','phone','is_active']
	search_fields=['name','email']




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


class helping_hand_admin(admin.ModelAdmin):
	list_display=['name_project','email','idea']


class battijalao_admin(admin.ModelAdmin):
	list_display=['course_name','email_id','idea']

class project_all_admin(admin.ModelAdmin):
	list_display=['project_title','project_class','project_price']


class project_postgrad_admin(admin.ModelAdmin):
	list_display=['project_Divison']

class project_undergrad_admin(admin.ModelAdmin):
	list_display=['project_Divison']

class project_research_admin(admin.ModelAdmin):
	list_display=['project_Divison']



admin.site.register(Enquiry,Enquiry_admin)


admin.site.register(user_reg, user_reg_admin)

admin.site.register(helping_hand, helping_hand_admin)
admin.site.register(batti_jalao, battijalao_admin)

admin.site.register(all_project, project_all_admin)
admin.site.register(project_undergrad, project_undergrad_admin)
admin.site.register(project_postgrad,project_postgrad_admin)
admin.site.register(project_research, project_research_admin)