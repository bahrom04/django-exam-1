from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Lesson, Topic, UserLessonRewiew
from .serializers import LessonSerializer, TopicSerializer, UserLessonRewiewSerializer
from django.views import View


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LessonListView(generics.ListAPIView, View):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserLessonRewiewView(generics.ListAPIView):
    queryset = UserLessonRewiew.objects.all()
    serializer_class = UserLessonRewiewSerializer

    def get_queryset(self):
        user = self.request.user
        user_lessons = UserLessonRewiew.objects.filter(user=user)
        lesson_ids = user_lessons.values_list('lesson__id', flat=True)
        return Lesson.objects.filter(id__in=lesson_ids)

