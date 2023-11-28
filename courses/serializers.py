from rest_framework import serializers
from .models import Product, Lesson, UserLessonRewiew


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserLessonRewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessonRewiew
        fields = '__all__'