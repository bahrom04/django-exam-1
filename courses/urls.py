from django.urls import path
from .views import TopicListView, LessonListView, UserLessonRewiewView

urlpatterns = [
    path('topic/', TopicListView.as_view(), name='topic'),
    path('lesson/', LessonListView.as_view(), name='lesson'),
    path('<slug:user>/review/', UserLessonRewiewView.as_view(), name='userreview'),
]