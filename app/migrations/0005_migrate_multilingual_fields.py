from django.db import migrations, models


def copy_uz_fields(apps, schema_editor):
    Category = apps.get_model("app", "Category")
    for obj in Category.objects.all():
        obj.name_uz = obj.name
        obj.save(update_fields=["name_uz"])

    Project = apps.get_model("app", "Project")
    for obj in Project.objects.all():
        obj.title_uz = obj.title
        obj.description_uz = obj.description
        obj.client_uz = obj.client
        obj.save(update_fields=["title_uz", "description_uz", "client_uz"])

    AboutUs = apps.get_model("app", "AboutUs")
    for obj in AboutUs.objects.all():
        obj.text_uz = obj.text
        obj.save(update_fields=["text_uz"])

    Profession = apps.get_model("app", "Profession")
    for obj in Profession.objects.all():
        obj.title_uz = obj.title
        obj.save(update_fields=["title_uz"])

    Team = apps.get_model("app", "Team")
    for obj in Team.objects.all():
        obj.first_name_uz = obj.first_name
        obj.last_name_uz = obj.last_name
        obj.save(update_fields=["first_name_uz", "last_name_uz"])

    Service = apps.get_model("app", "Service")
    for obj in Service.objects.all():
        obj.name_uz = obj.name
        obj.description_uz = obj.description
        obj.save(update_fields=["name_uz", "description_uz"])

    Contact = apps.get_model("app", "Contact")
    for obj in Contact.objects.all():
        obj.name_uz = obj.name
        obj.message_uz = obj.message
        obj.save(update_fields=["name_uz", "message_uz"])

    Comment = apps.get_model("app", "Comment")
    for obj in Comment.objects.all():
        obj.username_uz = obj.username
        obj.text_uz = obj.text
        obj.save(update_fields=["username_uz", "text_uz"])


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_add_multilingual_fields"),
    ]

    operations = [
        migrations.RunPython(copy_uz_fields, migrations.RunPython.noop),
        migrations.RemoveField(model_name="category", name="name"),
        migrations.RemoveField(model_name="project", name="title"),
        migrations.RemoveField(model_name="project", name="description"),
        migrations.RemoveField(model_name="project", name="client"),
        migrations.RemoveField(model_name="aboutus", name="text"),
        migrations.RemoveField(model_name="profession", name="title"),
        migrations.RemoveField(model_name="team", name="first_name"),
        migrations.RemoveField(model_name="team", name="last_name"),
        migrations.RemoveField(model_name="service", name="name"),
        migrations.RemoveField(model_name="service", name="description"),
        migrations.RemoveField(model_name="contact", name="name"),
        migrations.RemoveField(model_name="contact", name="message"),
        migrations.RemoveField(model_name="comment", name="text"),
        migrations.RemoveField(model_name="comment", name="username"),
        migrations.AlterField(
            model_name="category",
            name="name_uz",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_uz",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="title_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_uz",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="description_ar",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="client_uz",
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="client_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="client_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="client_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="text_uz",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="text_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="text_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="text_ar",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profession",
            name="title_uz",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="profession",
            name="title_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profession",
            name="title_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profession",
            name="title_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="first_name_uz",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="team",
            name="first_name_ru",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="first_name_en",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="first_name_ar",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="last_name_uz",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="team",
            name="last_name_ru",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="last_name_en",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="last_name_ar",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="name_uz",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="name_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="name_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="name_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="description_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="description_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="description_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="description_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name_uz",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name_ru",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name_en",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name_ar",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message_uz",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message_ar",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text_uz",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text_ar",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="username_uz",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="comment",
            name="username_ru",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="username_en",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="username_ar",
            field=models.CharField(max_length=150, blank=True, null=True),
        ),
    ]
