from django.db import models
from user.models import User
from common.models import BaseModel


class Topic(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='static/courses_images/')
    video_url   = models.URLField()
    duration    = models.IntegerField()
    price       = models.IntegerField()

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title
    

# User progress
class UserLessonRewiew(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    last_watched = models.DateTimeField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'UserRewiew'
        verbose_name_plural = 'UserRewiews'

    def __str__(self):
        return f"{self.user.username} - {self.video_lesson.title}"


