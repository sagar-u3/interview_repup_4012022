from rest_framework.serializers import ModelSerializer
from api.models import Board

class BoardCreateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Board

class BoardUpdateSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Board
        read_only_fields=['title']