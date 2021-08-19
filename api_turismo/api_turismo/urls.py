from django import urls
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from core.api.viewsets import PontosTuristicosViewSet
from atracaoes.api.viewsets import AtracoesViewSet
from endereco.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacaoes.api.viewsets import AvaliacaoViewSet
from rest_framework.authtoken.views import obtain_auth_token
 

#Rotas dos endpoints
router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet, basename = 'PontosTuristicos')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MIDIA_URL, document_root=settings.MIDIA_ROOT)
