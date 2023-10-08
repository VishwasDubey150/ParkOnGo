from django.urls import path,include
from rest_framework import routers
from Api import views
router = routers.DefaultRouter()
router.register(r'locality',views.LocalityViewSet)
router.register(r'stations',views.StationViewSet)
router.register(r'user',views.UserViewSet)
router.register(r'parking',views.ParkingViewSet)
router.register(r'partner',views.PartnerViewSet)
router.register(r'reservation',views.ReservationViewSet)
router.register(r'local_business',views.Local_BusinessViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
