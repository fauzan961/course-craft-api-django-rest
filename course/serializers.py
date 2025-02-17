from rest_framework import serializers
from .models import Course, Category, Lesson

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['slug', 'created_at']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent']
        
    def validate_parent(self, value):
        if value:
            if self.instance and value == self.instance:
                raise serializers.ValidationError("A category cannot be its own parent.")
            if value.parent is not None:
                raise serializers.ValidationError("A subcategory cannot have a parent that is also a subcategory.")
        return value
    
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['created_at']
        extra_kwargs = {
            'course': {'write_only': True}
        }
        
        
    