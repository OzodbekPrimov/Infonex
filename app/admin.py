from django.contrib import admin

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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "project_count")
    search_fields = ("name",)
    ordering = ("name",)

    @admin.display(description="Projects")
    def project_count(self, obj):
        return obj.projects.count()


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "client", "type_list", "link")
    list_filter = ("year", "type")
    search_fields = ("title", "client", "description")
    filter_horizontal = ("type",)
    inlines = (ProjectImageInline,)
    ordering = ("-year", "title")

    @admin.display(description="Categories")
    def type_list(self, obj):
        return ", ".join(obj.type.values_list("name", flat=True))


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")
    search_fields = ("project__title",)
    autocomplete_fields = ("project",)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "short_text")
    search_fields = ("text",)

    @admin.display(description="Text")
    def short_text(self, obj):
        return (obj.text[:60] + "...") if len(obj.text) > 60 else obj.text


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("title", "team_count")
    search_fields = ("title",)
    ordering = ("title",)

    @admin.display(description="Team members")
    def team_count(self, obj):
        return obj.team_members.count()


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "profession")
    list_filter = ("profession",)
    search_fields = ("first_name", "last_name")
    autocomplete_fields = ("profession",)
    ordering = ("last_name", "first_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_count")
    search_fields = ("name",)
    ordering = ("name",)

    @admin.display(description="Contacts")
    def contact_count(self, obj):
        return obj.contacts.count()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service")
    list_filter = ("service",)
    search_fields = ("name", "email", "message")
    autocomplete_fields = ("service",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "short_text")
    search_fields = ("username", "text")
    ordering = ("username",)

    @admin.display(description="Text")
    def short_text(self, obj):
        return (obj.text[:60] + "...") if len(obj.text) > 60 else obj.text
