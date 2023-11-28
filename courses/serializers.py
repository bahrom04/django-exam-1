from rest_framework import serializers
from .models import Topic, Lesson, UserLessonRewiew


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserLessonRewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessonRewiew
        fields = '__all__'