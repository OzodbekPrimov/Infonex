from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework import generics, permissions

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
from .serializers import (
    AboutUsSerializer,
    CategorySerializer,
    CommentSerializer,
    ContactSerializer,
    ProfessionSerializer,
    ProjectImageSerializer,
    ProjectSerializer,
    ServiceSerializer,
    TeamSerializer,
)
from .tasks import send_contact_notification


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        return bool(user and user.is_authenticated and user.is_superuser)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrReadOnly]


@extend_schema(
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
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.query_params.get("category")
        if category and category.isdigit():
            queryset = queryset.filter(type__id=int(category))
        return queryset.distinct()


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ProjectImageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ProjectImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class AboutUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ProfessionListCreateView(generics.ListCreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ProfessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def perform_create(self, serializer):
        contact = serializer.save()
        send_contact_notification.delay(contact.id)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsSuperuserOrReadOnly]
