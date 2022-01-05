from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin 
from api.models import Board
from api.serializers import BoardCreateSerializer, BoardUpdateSerializer

class BoardViewset(GenericViewSet, CreateModelMixin, UpdateModelMixin):
    queryset = Board.objects.all()
    def get_serializer_class(self):
        if self.action=="list":
            return BoardCreateSerializer
        if self.action=="update":
            return BoardUpdateSerializer