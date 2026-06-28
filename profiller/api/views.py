from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil
from profiller.api.serializers import ProfilSerailizer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliYaDaReadOnly


class ProfilViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerailizer
    permission_classes = [IsAuthenticated, KendiProfiliYaDaReadOnly]



# Django Restframework B-3 Ders-9 Viewsets ve Routers Part 2 GenericViewSet ve Mixinsler
