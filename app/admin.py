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
    FAQ,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_uz", "project_count")
    search_fields = ("name_uz", "name_ru", "name_en", "name_ar")
    ordering = ("name_uz",)
    fieldsets = (
        ("Uzbek", {"fields": ("name_uz",)}),
        ("Russian", {"fields": ("name_ru",)}),
        ("English", {"fields": ("name_en",)}),
        ("Arabic", {"fields": ("name_ar",)}),
    )

    @admin.display(description="Projects")
    def project_count(self, obj):
        return obj.projects.count()


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title_uz", "year", "client", "category_list", "service_list", "link")
    list_filter = ("year", "category", "services")
    search_fields = (
        "title_uz",
        "title_ru",
        "title_en",
        "title_ar",
        "client",
        "description_uz",
        "description_ru",
        "description_en",
        "description_ar",
    )
    filter_horizontal = ("category", "services")
    inlines = (ProjectImageInline,)
    ordering = ("-year", "title_uz")
    fieldsets = (
        (
            "Uzbek",
            {"fields": ("title_uz", "description_uz")},
        ),
        (
            "Russian",
            {"fields": ("title_ru", "description_ru")},
        ),
        (
            "English",
            {"fields": ("title_en", "description_en")},
        ),
        (
            "Arabic",
            {"fields": ("title_ar", "description_ar")},
        ),
        (
            "Details",
            {"fields": ("category", "services", "client", "link", "year")},
        ),
    )

    @admin.display(description="Categories")
    def category_list(self, obj):
        return ", ".join(obj.category.values_list("name_uz", flat=True))

    @admin.display(description="Services")
    def service_list(self, obj):
        return ", ".join(obj.services.values_list("name_uz", flat=True))


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")
    search_fields = ("project__title_uz",)
    autocomplete_fields = ("project",)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "short_text_uz")
    search_fields = ("text_uz", "text_ru", "text_en", "text_ar")
    fieldsets = (
        ("Uzbek", {"fields": ("text_uz",)}),
        ("Russian", {"fields": ("text_ru",)}),
        ("English", {"fields": ("text_en",)}),
        ("Arabic", {"fields": ("text_ar",)}),
        ("Media", {"fields": ("image",)}),
    )

    @admin.display(description="Text (UZ)")
    def short_text_uz(self, obj):
        return (obj.text_uz[:60] + "...") if len(obj.text_uz) > 60 else obj.text_uz


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("title_uz", "team_count")
    search_fields = ("title_uz", "title_ru", "title_en", "title_ar")
    ordering = ("title_uz",)
    fieldsets = (
        ("Uzbek", {"fields": ("title_uz",)}),
        ("Russian", {"fields": ("title_ru",)}),
        ("English", {"fields": ("title_en",)}),
        ("Arabic", {"fields": ("title_ar",)}),
    )

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
    fieldsets = (
        (
            "Details",
            {"fields": ("first_name", "last_name", "profession", "image")},
        ),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name_uz", "contact_count", "order")
    search_fields = ("name_uz", "name_ru", "name_en", "name_ar")
    list_editable = ('order',)
    ordering = ("name_uz",)
    fieldsets = (
        (
            "Uzbek",
            {"fields": ("name_uz", "description_uz")},
        ),
        (
            "Russian",
            {"fields": ("name_ru", "description_ru")},
        ),
        (
            "English",
            {"fields": ("name_en", "description_en")},
        ),
        (
            "Arabic",
            {"fields": ("name_ar", "description_ar")},
        ),
    )

    @admin.display(description="Contacts")
    def contact_count(self, obj):
        return obj.contacts.count()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service")
    list_filter = ("service",)
    search_fields = ("name", "message", "email")
    autocomplete_fields = ("service",)
    fieldsets = (
        ("Details", {"fields": ("name", "message", "email", "service")}),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("username_uz", "short_text_uz")
    search_fields = (
        "username_uz",
        "username_ru",
        "username_en",
        "username_ar",
        "text_uz",
        "text_ru",
        "text_en",
        "text_ar",
    )
    ordering = ("username_uz",)
    fieldsets = (
        ("Uzbek", {"fields": ("username_uz", "text_uz")}),
        ("Russian", {"fields": ("username_ru", "text_ru")}),
        ("English", {"fields": ("username_en", "text_en")}),
        ("Arabic", {"fields": ("username_ar", "text_ar")}),
        ("Media", {"fields": ("image",)}),
    )

    @admin.display(description="Text (UZ)")
    def short_text_uz(self, obj):
        return (obj.text_uz[:60] + "...") if len(obj.text_uz) > 60 else obj.text_uz


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question_uz", "answer_uz")

    search_fields = (
        "question_uz", "answer_uz",
        "question_en", "answer_en",
        "question_ru", "answer_ru",
        "question_ar", "answer_ar",
    )

    fieldsets = (
        "Uzbek", {"field": ("question_uz", "answer_uz")},
        "Russian", {"field": ("question_ru", "answer_ru")},
        "English", {"field": ("question_en", "answer_en")},
        "Arabic", {"field": ("question_ar", "answer_ar")},
    )