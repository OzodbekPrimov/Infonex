from django.utils.translation import get_language
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

LANGUAGE_CODES = ("uz", "ru", "en", "ar")


class TranslatedFieldsMixin:
    translated_fields = ()

    def _normalize_language(self, code: str | None) -> str:
        if not code:
            return "uz"
        normalized = code.lower().replace("_", "-").split("-")[0]
        return normalized if normalized in LANGUAGE_CODES else "uz"

    def _get_language(self) -> str:
        request = self.context.get("request")
        if request is not None:
            return self._normalize_language(getattr(request, "LANGUAGE_CODE", None))
        return self._normalize_language(get_language())

    def get_fields(self):
        fields = super().get_fields()
        for base in self.translated_fields:
            if base not in fields:
                fields[base] = serializers.CharField(read_only=True)
            for code in LANGUAGE_CODES:
                field_name = f"{base}_{code}"
                if field_name in fields:
                    fields[field_name].write_only = True
        return fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        lang = self._get_language()
        for base in self.translated_fields:
            value = data.get(f"{base}_{lang}")
            if value in ("", None):
                value = data.get(f"{base}_uz")
            data[base] = value
            for code in LANGUAGE_CODES:
                data.pop(f"{base}_{code}", None)
        return data

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if self.partial:
            return attrs
        errors = {}
        model = self.Meta.model
        for base in self.translated_fields:
            uz_field = f"{base}_uz"
            model_field = model._meta.get_field(uz_field)
            if model_field.blank:
                continue
            value = attrs.get(uz_field)
            if value in ("", None):
                if self.instance and getattr(self.instance, uz_field, None):
                    continue
                errors[uz_field] = ["This field is required."]
        if errors:
            raise serializers.ValidationError(errors)
        return attrs


class CategorySerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    translated_fields = ("name",)

    class Meta:
        model = Category
        fields = "__all__"


class ProjectSerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    translated_fields = ("title", "description")

    class Meta:
        model = Project
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())

    class Meta:
        model = ProjectImage
        fields = "__all__"


class AboutUsSerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    image = serializers.ImageField()
    translated_fields = ("text",)

    class Meta:
        model = AboutUs
        fields = "__all__"


class ProfessionSerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    translated_fields = ("title",)

    class Meta:
        model = Profession
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())

    class Meta:
        model = Team
        fields = "__all__"


class ServiceSerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    translated_fields = ("name", "description")

    class Meta:
        model = Service
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class CommentSerializer(TranslatedFieldsMixin, serializers.ModelSerializer):
    image = extend_schema_field(OpenApiTypes.BINARY)(serializers.ImageField())
    translated_fields = ("username", "text")

    class Meta:
        model = Comment
        fields = "__all__"
