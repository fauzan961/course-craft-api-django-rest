from django.db import models
from user.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def clean(self):
        if self.parent:
            if self.parent == self:
                raise ValidationError("A category cannot be its own parent!")
            if self.parent.parent is not None:
                raise ValidationError("A subcategory cannot have a parent that is also a subcategory!")
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS_CHOICES = [('draft', 'Draft'),
                      ('published', 'Published'),
                      ('in-review', 'In Review'),
                      ('rejected', 'Rejected'),]
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    categories = models.ManyToManyField(Category, related_name='courses', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='lesson_videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    duration = models.DurationField()
    order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title