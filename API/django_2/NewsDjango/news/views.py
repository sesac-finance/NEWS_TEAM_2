from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TbDomain
from .serializers import TestDataSerializer

# 장고에 뉴스데이터 프레임을 올려놔라
# 리턴하기전에 Function에서 부른다고 생각하면됨 
# news_df = pd.read_csv()
@api_view(['GET'])
def getTbDomain(request):
    datas = TbDomain.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTbDomain_one(request, name):
    print(name)
    # 추천 로직 
    # news_list = recommend(target_news, news_df)
    # object가 아니니 , tbnews.objects.filter(pk__in=[])

    data = TbDomain.objects.get(name=name)
    # data = TbDomain.objects.get(name(컬럼명)=name(입력값))
    serializer = TestDataSerializer(data, many=False)
    return Response(serializer.data)