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
    category = ProjectCategorySerializer(read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True, source='images')  # برای نمایش تصاویر گالری

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')  # اگر BaseModel این فیلدها را داشته باشد