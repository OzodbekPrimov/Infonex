from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiTypes,
    extend_schema,
    extend_schema_view,
)
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser

from .models import (
    FAQ,
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
from .serializers import (
    AboutUsSerializer,
    CategorySerializer,
    CommentSerializer,
    ContactSerializer,
    FAQModelSerializer,
    ProfessionSerializer,
    ProjectCreateSerializer,
    ProjectImageSerializer,
    ProjectListSerializer,
    ServiceSerializer,
    TeamListSerializer,
    TeamSerializer,
)
from .tasks import send_contact_notification


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        return bool(user and user.is_authenticated and user.is_superuser)


@extend_schema(tags=["Category"])
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(tags=["Category"])
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(
    tags=["Project"],
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Filter by Category ID",
        )
    ]
)
class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.query_params.get("category")
        if category and category.isdigit():
            queryset = queryset.filter(category__id=int(category))
        return queryset.distinct()


@extend_schema(tags=["Project"])
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(tags=["Project"])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(
    tags=["ProjectImage"],
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "image": {"type": "string", "format": "binary"},
                "project": {"type": "integer"},
                "is_main": {"type": "boolan"},
            },
            "required": ["image", "project"],
        }
    },
    responses=ProjectImageSerializer,
    methods=["POST"],
)
class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(tags=["ProjectImage"])
@extend_schema_view(
    tags=["ProjectImage"],
    put=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "project": {"type": "integer"},
                },
                "required": ["image", "project"],
            }
        },
        responses=ProjectImageSerializer,
    ),
    patch=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "project": {"type": "integer"},
                },
            }
        },
        responses=ProjectImageSerializer,
    ),
)
class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(
    tags=["AboutUs"],
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "image": {"type": "string", "format": "binary"},
                "text_uz": {"type": "string"},
                "text_ru": {"type": "string"},
                "text_en": {"type": "string"},
                "text_ar": {"type": "string"},
            },
            "required": ["image", "text_uz"],
        }
    },
    responses=AboutUsSerializer,
)
class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(tags=["AboutUs"])
@extend_schema_view(
    tags=["AboutUs"],
    put=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "text_uz": {"type": "string"},
                    "text_ru": {"type": "string"},
                    "text_en": {"type": "string"},
                    "text_ar": {"type": "string"},
                },
                "required": ["image", "text_uz"],
            }
        },
        responses=AboutUsSerializer,
    ),
    patch=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "text_uz": {"type": "string"},
                    "text_ru": {"type": "string"},
                    "text_en": {"type": "string"},
                    "text_ar": {"type": "string"},
                },
            }
        },
        responses=AboutUsSerializer,
    ),
)
class AboutUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(tags=["Profession"])
class ProfessionListCreateView(generics.ListCreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(tags=["Profession"])
class ProfessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(
    tags=["Team"],
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "image": {"type": "string", "format": "binary"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "profession": {"type": "integer"},
            },
            "required": ["image", "first_name", "last_name", "profession"],
        }
    },
    responses=TeamSerializer,
    methods=["POST"],
)
class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TeamListSerializer
        return TeamSerializer


@extend_schema(tags=["Team"])
@extend_schema_view(
    tags=["Team"],
    put=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "profession": {"type": "integer"},
                },
                "required": ["image", "first_name", "last_name", "profession"],
            }
        },
        responses=TeamSerializer,
    ),
    patch=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "profession": {"type": "integer"},
                },
            }
        },
        responses=TeamSerializer,
    ),
)
class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(tags=["Service"])
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(tags=["Service"])
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(tags=["Contact"])
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()
        send_contact_notification.delay(contact.id)


@extend_schema(
    tags=["Comment"],
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "image": {"type": "string", "format": "binary"},
                "username_uz": {"type": "string"},
                "username_ru": {"type": "string"},
                "username_en": {"type": "string"},
                "username_ar": {"type": "string"},
                "text_uz": {"type": "string"},
                "text_ru": {"type": "string"},
                "text_en": {"type": "string"},
                "text_ar": {"type": "string"},
            },
            "required": ["image", "username_uz", "text_uz"],
        }
    },
    responses=CommentSerializer,
    methods=["POST"],
)
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    parser_classes = [MultiPartParser]


@extend_schema(tags=["Comment"])
@extend_schema_view(
    tags=["Comment"],
    put=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "username_uz": {"type": "string"},
                    "username_ru": {"type": "string"},
                    "username_en": {"type": "string"},
                    "username_ar": {"type": "string"},
                    "text_uz": {"type": "string"},
                    "text_ru": {"type": "string"},
                    "text_en": {"type": "string"},
                    "text_ar": {"type": "string"},
                },
                "required": ["image", "username_uz", "text_uz"],
            }
        },
        responses=CommentSerializer,
    ),
    patch=extend_schema(
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {"type": "string", "format": "binary"},
                    "username_uz": {"type": "string"},
                    "username_ru": {"type": "string"},
                    "username_en": {"type": "string"},
                    "username_ar": {"type": "string"},
                    "text_uz": {"type": "string"},
                    "text_ru": {"type": "string"},
                    "text_en": {"type": "string"},
                    "text_ar": {"type": "string"},
                },
            }
        },
        responses=CommentSerializer,
    ),
)
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    parser_classes = [MultiPartParser]


@extend_schema(tags=["FAQ"], request=FAQModelSerializer)
class FAQCreateAPIView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer


@extend_schema(tags=["FAQ"], request=FAQModelSerializer)
class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer


@extend_schema(tags=["FAQ"], request=FAQModelSerializer)
class FAQUpdateAPIView(generics.UpdateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer
    lookup_field = "id"


@extend_schema(tags=["FAQ"], request=FAQModelSerializer)
class FAQDeleteAPIView(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer
    lookup_field = "id"
