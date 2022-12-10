from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TbComment, TbDomain, TbNews, TbUser #1
from .serializers import TbNewsSerializer,NewsRecommenSerializer #2
from rest_framework import status
import pandas as pd


@api_view(['GET'])
def getNews(request, newsid):
    news = get_object_or_404(TbNews, pk=newsid)
    serializer = TbNewsSerializer(news)
    return Response(serializer.data, status=status.HTTP_200_OK)

# /news/all/
@api_view(['GET'])
def getTbNewsAll(request):
    print('****'*10)
    print('### 최신뉴스 5개를 출력합니다.')
    data = TbNews.objects.all().order_by('writedat')[0:5] #1 # 받아올 페이지 
    serializer = TbNewsSerializer(data, many=True) #2
    return Response(serializer.data)  


#/news/press/"언론사명"
@api_view(['GET'])
def getNewsPerPress(request,press):
    print('****'*10)
    print(f'### {press}에서 최근 5개의 뉴스을 추천합니다.')
    data = TbNews.objects.filter(press=press).order_by('writedat')[:5] #1 # 받아올 페이지 
    serializer = TbNewsSerializer(data, many=True) #2
    return Response(serializer.data)  

#/news/mCategory/"카테고리"
@api_view(['GET'])
def getNewsPerMCategory(request,maincategory):
    print('****'*10)
    print(f'### {maincategory}에서 최근 5개의 뉴스을 추천합니다.')
    data = TbNews.objects.filter(maincategory=maincategory).order_by('writedat')[:5] #1 # 받아올 페이지 
    serializer = TbNewsSerializer(data, many=True) #2
    return Response(serializer.data)  


recommend_list = pd.read_csv('./data/recommend_dataframe.csv',index_col=0)

#up-to-date/recomm_news
@api_view(['GET'])
def getNewsRecommend(request,newsid):

    print('****'*10)
    print(f'### {newsid}와(과)) 유사한 최근 5개의 뉴스을 추천합니다.')

    recommend_l=recommend_list[recommend_list['newsid']==newsid]['recommend_list']
    recommend=TbNews.objects.filter(pk__in=tuple(map(int, recommend_l.values[0][1:-1].split(','))))
    serializer = NewsRecommenSerializer(recommend, many=True) #2
    return Response(serializer.data)