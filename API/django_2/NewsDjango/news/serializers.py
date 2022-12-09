from rest_framework.serializers import ModelSerializer
from .models import TbComment, TbDomain, TbNews, TbUser


class TestDataSerializer(ModelSerializer):
    class Meta:
        model = TbDomain
        fields = '__all__'

class TbUserSerializer(ModelSerializer):
    class Meta:
        model = TbUser
        fields = '__all__'

class TbNewsSerializer(ModelSerializer):
    class Meta:
        model = TbNews
        # fields = ('id','domainid','maincategory','subcategory','writedat','title','content','url','press')
        fields = ('id','title','content','url','press',)

class NewsRecommenSerializer(ModelSerializer):
    class Meta:
        model = TbNews
        fields = ('id','title','url','writedat')
