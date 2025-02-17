from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CategoryViewSet, SubcategoryView, LessonViewSet, CourseLessonsView

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('categories', CategoryViewSet, basename='category')
router.register('lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
    path('subcategories/<str:category>', SubcategoryView.as_view(), name='subcategory-list'),
    path('course-lessons/<str:course_slug>', CourseLessonsView.as_view(), name='course-lessons'),
]