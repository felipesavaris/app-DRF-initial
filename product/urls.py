from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet


route = DefaultRouter()
route.register(r'product', ProductViewSet, basename='Product')

urlpatterns = route.urls
