from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from employee.views import EmployeeViewSet, LocationViewSet, DepartmentViewSet
from ChatGPT.views import GPTViewSet


router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'gpt', GPTViewSet, basename='gpt')

schema_view = get_schema_view(
    openapi.Info(
        title="API 문서",
        default_version="v1",
        description="eco&rich API 문서",
        terms_of_service="#",
        contact=openapi.Contact(email="yya71bb@naver.com"),
        license=openapi.License(name="이병준"),
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>\.json|\.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
