from rest_framework import viewsets

from .models import MenuModel
from .serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return MenuModel.objects.all()
