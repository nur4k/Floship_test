from django.urls import path

from rest_framework.routers import DefaultRouter

from store.views import StoreView


router = DefaultRouter()
router.register('all', StoreView)

urlpatterns = []
urlpatterns += router.urls
