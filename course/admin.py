from django.contrib import admin
from .models import Course, Category, Lesson

class CustomCourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('title', 'slug', 'price', 'status')

class CustomCategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'slug', 'parent')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CustomLessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = ('title', 'course', 'duration')

admin.site.register(Course, CustomCourseAdmin)
admin.site.register(Category, CustomCategoryAdmin)
admin.site.register(Lesson, CustomLessonAdmin)