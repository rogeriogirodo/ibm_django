from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'question_grade', 'course']
    search_fields = ['question_text', 'course__name']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['id','enrollment']
    search_fields = ['user__name', 'course__name']
    def has_add_permission(self, request, obj=None):
        return False

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course','user']
    def has_add_permission(self, request, obj=None):
        return False

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)