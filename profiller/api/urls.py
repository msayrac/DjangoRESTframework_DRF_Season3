from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller', ProfilViewSet)
router.register(r'durum', ProfilDurumViewSet)

urlpatterns = [    
    path('', include(router.urls)),
   
]

# profil_list = ProfilViewSet.as_view({'get':'list'})
# profil_detail = ProfilViewSet.as_view({'get':'retrieve'})


# urlpatterns = [    
#     path('kullanici-profilleri/', profil_list, name='profiller'),
#     path('kullanici-profilleri/<int:pk>/', profil_detail, name='profil-detay' ),
# ]

