from django.contrib import admin
from .models import Exam, Quiz

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'time_limit_minutes')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'start_date', 'end_date', 'time_limit_minutes')



@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question', 'correct_option')
    list_filter = ('exam',)

    def get_queryset(self, request):

        qs = super().get_queryset(request)
        return qs.select_related('exam')
