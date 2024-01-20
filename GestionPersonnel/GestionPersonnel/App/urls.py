from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views


router = DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),
    path('home/', home),
    path('rendez-vous/', appointment),
    path('consultations/', consultations),
    path('prescription/', prescription),
    path('file-d-attente/', file_d_attente),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('patient/', patient),
    path('dispo/',DisponibiliteListAPIView.as_view(), name='api-view'),
    path('disponibilite/',views.AjoutDisponibilite.as_view(), name='ajout_dispo'),
    path('rdv/', create_rdv),
]
