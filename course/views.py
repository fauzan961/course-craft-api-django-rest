from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Course, Category, Lesson
from .serializers import CourseSerializer, CategorySerializer, LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(parent__isnull=True)
        return self.queryset
    
class SubcategoryView(APIView):
    def get(self, request, category):
        category_instance = get_object_or_404(Category, slug=category)
        subcategories = category_instance.subcategories.all()
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data)
    
class LessonViewSet(viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    
class CourseLessonsView(APIView):
    def get(self, request, course_slug):
        course = get_object_or_404(Course, slug=course_slug)
        lessons = Lesson.objects.filter(course = course)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    