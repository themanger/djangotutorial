from django.contrib import admin

from .models import Choice, Question




class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    fieldsets = [
        ('Question name', {'fields' : ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]



admin.site.register(Question, QuestionAdmin)

# Register your models here.
