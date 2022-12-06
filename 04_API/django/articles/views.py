from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleSerializer
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def detail(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def list_article(request):

    if request.method == 'GET': # 조회
        articles = get_list_or_404(Article)
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST': # 생성
        articles = get_list_or_404(Article, pk=1)
        serializer = ArticleSerializer(articles)
        
        return Response(serializer.data, status=status.HTTP_200_OK)