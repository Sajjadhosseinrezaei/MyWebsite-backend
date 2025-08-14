from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # اختیاری برای امنیت بیشتر
from .models import Profile, Skill, Technology, ProjectCategory, Project, ProjectImage
from .serializers import (
    ProfileSerializer, SkillSerializer, TechnologySerializer,
    ProjectCategorySerializer, ProjectSerializer, ProjectImageSerializer
)

# برای Profile: تک رکورد، پس RetrieveAPIView استفاده می‌کنیم (فرض بر single instance)
class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # اختیاری: فقط خواندنی برای کاربران عمومی

    def get_object(self):
        # فرض بر این که فقط یک پروفایل وجود دارد؛ اگر چند تا باشد، از ID استفاده کنید
        return Profile.objects.first()

# برای Skill: لیست مهارت‌ها، ReadOnlyModelViewSet
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# برای Technology: لیست تکنولوژی‌ها، ReadOnlyModelViewSet
class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# برای ProjectCategory: لیست دسته‌بندی‌ها، ReadOnlyModelViewSet
class ProjectCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# برای Project: لیست پروژه‌ها، ReadOnlyModelViewSet
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # اختیاری: فیلتر بر اساس featured یا category اگر نیاز باشد
    def get_queryset(self):
        queryset = super().get_queryset()
        featured = self.request.query_params.get('featured')
        if featured:
            queryset = queryset.filter(is_featured=True)
        return queryset
    
    def get_serializer_context(self):
        """
        این متد context را به سریالایزر اضافه می‌کند.
        """
        return {'request': self.request}

# برای ProjectImage: تصاویر وابسته به پروژه، می‌توان ViewSet جداگانه داشت اما بهتر است nested باشد
# اما برای سادگی، ReadOnlyModelViewSet با فیلتر بر اساس project
class ProjectImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset