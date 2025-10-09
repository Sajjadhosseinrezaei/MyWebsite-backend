from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileView, SkillViewSet, TechnologyViewSet,
    ProjectCategoryViewSet, ProjectViewSet, ProjectImageViewSet, ContactView
)
from .health import health_check

# استفاده از DefaultRouter برای ViewSetها (که لیست و جزئیات را مدیریت می‌کند)
router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')  # URLها: /skills/ (لیست), /skills/{id}/ (جزئیات)
router.register(r'technologies', TechnologyViewSet, basename='technology')  # /technologies/, /technologies/{id}/
router.register(r'project-categories', ProjectCategoryViewSet, basename='projectcategory')  # /project-categories/, /project-categories/{id}/
router.register(r'projects', ProjectViewSet, basename='project')  # /projects/, /projects/{id}/
router.register(r'project-images', ProjectImageViewSet, basename='projectimage')  # /project-images/, /project-images/{id}/ (با فیلتر ?project=id)

# URLهای دستی برای ویوهای غیر ViewSet مثل Profile
urlpatterns = [
    path('', include(router.urls)),  # همه URLهای router
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('contact/', ContactView.as_view(), name='contact'),
    path('health/', health_check, name='health-check'),
]
