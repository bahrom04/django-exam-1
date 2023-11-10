from django.shortcuts import render
from .serializers import NewsSerializer, SocialsSerializer
from .models import News, Socials
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# class NewsPaginationMain(PageNumberPagination):
#     page_size = 2 
#     # Related news limit 3
#     page_size_query_param = 'page_size'
#     max_page_size = 20 
    

# example: /api/news/?size=3 returns 3 news per page
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'  # items per page


class SocialView(generics.ListAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer
    

class NewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPageNumberPagination

    






