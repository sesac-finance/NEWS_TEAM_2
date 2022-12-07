from rest_framework.serializers import ModelSerializer
from .models import TbDomain

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = TbDomain
        fields = '__all__'
