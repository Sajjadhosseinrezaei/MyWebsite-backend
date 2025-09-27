from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # اختیاری برای امنیت بیشتر
from .models import Profile, Skill, Technology, ProjectCategory, Project, ProjectImage
from .serializers import (
    ProfileSerializer, SkillSerializer, TechnologySerializer,
    ProjectCategorySerializer, ProjectSerializer, ProjectImageSerializer,
    ContactSerializer
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
import requests
from email.utils import parseaddr
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



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
    

class ContactView(APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'success': False, 'message': 'اطلاعات نامعتبر', 'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        token = data.get('turnstile_token')

        # اعتبارسنجی توکن Turnstile
        secret = getattr(settings, 'TURNSTILE_SECRET_KEY', None)
        if not secret:
            return Response({'success': False, 'message': 'سرور پیکربندی نشده'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        verify_url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
        payload = {'secret': secret, 'response': token}

        try:
            resp = requests.post(verify_url, data=payload, timeout=10)
            resp.raise_for_status()
            result = resp.json()
        except requests.RequestException as e:
            return Response({'success': False, 'message': 'خطا در بررسی کپچا: ' + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not result.get('success'):
            return Response({'success': False, 'message': 'اعتبارسنجی کپچا ناموفق بود.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # ارسال ایمیل
        subject = data.get('subject') or f'پیام از {data.get("name")}'
        body = f"""
نام: {data.get('name')}
ایمیل: {data.get('email')}
موضوع: {data.get('subject')}

پیام:
{data.get('message')}
"""

        # parse و validate ایمیل‌ها
        raw_from = getattr(settings, 'MAIL_FROM', '')
        raw_to = getattr(settings, 'CONTACT_RECIPIENT_EMAIL', '')

        _, from_email = parseaddr(raw_from)
        _, to_email = parseaddr(raw_to)

        # validate
        try:
            validate_email(from_email)
            validate_email(to_email)
        except ValidationError:
            return Response({'success': False, 'message': 'آدرس ایمیل پیکربندی شده نامعتبر است.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=from_email,
                recipient_list=[to_email],
                fail_silently=False,
            )
        except Exception as e:
            return Response({'success': False, 'message': 'خطا در ارسال ایمیل: ' + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success': True, 'message': 'پیام ارسال شد.'})