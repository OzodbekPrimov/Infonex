from drf_spectacular.utils import OpenApiTypes, extend_schema_field
from rest_framework import serializers

from .models import (
    AboutUs,
    Category,
    Comment,
    Contact,
    Profession,
    Project,
    ProjectImage,
    Service,
    Team,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())

    class Meta:
        model = ProjectImage
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
            "title_ar",
            "description_uz",
            "description_ru",
            "description_en",
            "description_ar",
            "type",
            "link",
            "client",
            "year",
            "images",
        ]
      





class AboutUsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = AboutUs
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())

    class Meta:
        model = Team
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())

    class Meta:
        model = Comment
        fields = "__all__"
