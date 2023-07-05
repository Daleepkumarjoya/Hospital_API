from django.urls import path, include
from . import views
from django.urls import path, include
# from .views import
from rest_framework import routers

from .views import HomeModelViewSet, ServicesModelViewSet, AboutModelViewSet, DoctorsModelViewSet, BookModelViewSet, \
    ReviewModelViewSet, commentModelViewSet, ContactModelViewSet

router = routers.DefaultRouter()
router.register('Home', HomeModelViewSet)
router.register('Service', ServicesModelViewSet)
router.register('about', AboutModelViewSet)
router.register('doctor', DoctorsModelViewSet)
router.register('book', BookModelViewSet)
router.register('review', ReviewModelViewSet)
router.register('comment', commentModelViewSet)
router.register('contact', ContactModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
