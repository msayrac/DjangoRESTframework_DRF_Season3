from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerailizer, ProfilDurumSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliYaDaReadOnly, DurumSahibiYaDaReadOnly


class ProfilViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerailizer
    permission_classes = [IsAuthenticated, KendiProfiliYaDaReadOnly]




class ProfilDurumViewSet(ModelViewSet):
    queryset = ProfilDurum.objects.all()
    serializer_class = ProfilDurumSerializer
    permission_classes = [IsAuthenticated, DurumSahibiYaDaReadOnly]

    def perform_create(self, serializer):
        user_profil = self.request.user.profil
        serializer.save(user_profil=user_profil)
