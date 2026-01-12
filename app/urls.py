from django.urls import path

from .views import (
    AboutUsDetailView,
    AboutUsListCreateView,
    CategoryDetailView,
    CategoryListCreateView,
    CommentDetailView,
    CommentListCreateView,
    ContactCreateView,
    ProfessionDetailView,
    ProfessionListCreateView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectImageDetailView,
    ProjectImageListCreateView,
    ProjectListView,
    ServiceDetailView,
    ServiceListCreateView,
    TeamDetailView,
    TeamListCreateView,
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path(
        "categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"
    ),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("project/create",ProjectCreateView.as_view()),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path(
        "project-images/",
        ProjectImageListCreateView.as_view(),
        name="project-image-list-create",
    ),
    path(
        "project-images/<int:pk>/",
        ProjectImageDetailView.as_view(),
        name="project-image-detail",
    ),
    path("about-us/", AboutUsListCreateView.as_view(), name="about-us-list-create"),
    path("about-us/<int:pk>/", AboutUsDetailView.as_view(), name="about-us-detail"),
    path(
        "professions/", ProfessionListCreateView.as_view(), name="profession-list-create"
    ),
    path(
        "professions/<int:pk>/",
        ProfessionDetailView.as_view(),
        name="profession-detail",
    ),
    path("team/", TeamListCreateView.as_view(), name="team-list-create"),
    path("team/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("services/", ServiceListCreateView.as_view(), name="service-list-create"),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
    path("contact/", ContactCreateView.as_view(), name="contact-create"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
