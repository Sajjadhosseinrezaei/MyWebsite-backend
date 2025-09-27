from rest_framework import serializers
from .models import Profile, Skill, Technology, ProjectCategory, Project, ProjectImage

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at') 

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # این موارد به درستی از قبل تعریف شده بودند
    category = ProjectCategorySerializer(read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    
    # اینجا از سریالایزر اصلاح شده بالا استفاده می‌کنیم
    images = ProjectImageSerializer(many=True, read_only=True)

    # فیلد جدید برای آدرس کامل تصویر اصلی پروژه
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        # به جای '__all__' فیلدها را دستی لیست می‌کنیم
        fields = [
            'id',
            'title',
            'description',
            'short_description',
            'featured_image_url', # <-- فیلد جدید جایگزین شد
            'github_url',
            'demo_url',
            'status',
            'is_featured',
            'order',
            'category',
            'technologies',
            'images',
            'created_at',
            'updated_at',
        ]
    
    def get_featured_image_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image and hasattr(obj.featured_image, 'url'):
            return request.build_absolute_uri(obj.featured_image.url)
        return None




class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255, required=False, allow_blank=True)
    message = serializers.CharField()
    turnstile_token = serializers.CharField()  # از فرانت ارسال می‌شود
