from django.contrib import admin

from .models import Question, Choice



class ChoiceInline(admin.TabularInline): #admin.StackedInline
	model = Choice
	extra = 3

# 创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register()	
class QuestionAdmian(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	fieldsets = [
		(None,			   {'fields':['question_text']}),
		('Dateinfomation', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')



admin.site.register(Question, QuestionAdmian)
# admin.site.register(Choice)

# Register your models here.
