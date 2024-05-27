from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'products', views.ProductViewSet)




from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My first api project",
        default_version='v2',
        description="Simply learning how to create apis with django_rest_framework",
        terms_of_service="https://www.example.com/policies/terms/",

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


from django.conf  import settings
from django.conf.urls.static import static
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    #this urls is for swagger i.e. UI to views our API endpoints and their documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)