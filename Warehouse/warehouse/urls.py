from rest_framework.routers import DefaultRouter 

from warehouse.views import WareView

router = DefaultRouter()

router.register('add', WareView)

urlpatterns = []

urlpatterns += router.urls
