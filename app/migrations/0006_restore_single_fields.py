from django.db import migrations, models


def copy_single_fields(apps, schema_editor):
    Project = apps.get_model("app", "Project")
    for obj in Project.objects.all():
        obj.client = obj.client_uz
        obj.save(update_fields=["client"])

    Team = apps.get_model("app", "Team")
    for obj in Team.objects.all():
        obj.first_name = obj.first_name_uz
        obj.last_name = obj.last_name_uz
        obj.save(update_fields=["first_name", "last_name"])

    Contact = apps.get_model("app", "Contact")
    for obj in Contact.objects.all():
        obj.name = obj.name_uz
        obj.message = obj.message_uz
        obj.save(update_fields=["name", "message"])


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_migrate_multilingual_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="client",
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name="team",
            name="first_name",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="last_name",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="message",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.RunPython(copy_single_fields, migrations.RunPython.noop),
        migrations.RemoveField(model_name="project", name="client_uz"),
        migrations.RemoveField(model_name="project", name="client_ru"),
        migrations.RemoveField(model_name="project", name="client_en"),
        migrations.RemoveField(model_name="project", name="client_ar"),
        migrations.RemoveField(model_name="team", name="first_name_uz"),
        migrations.RemoveField(model_name="team", name="first_name_ru"),
        migrations.RemoveField(model_name="team", name="first_name_en"),
        migrations.RemoveField(model_name="team", name="first_name_ar"),
        migrations.RemoveField(model_name="team", name="last_name_uz"),
        migrations.RemoveField(model_name="team", name="last_name_ru"),
        migrations.RemoveField(model_name="team", name="last_name_en"),
        migrations.RemoveField(model_name="team", name="last_name_ar"),
        migrations.RemoveField(model_name="contact", name="name_uz"),
        migrations.RemoveField(model_name="contact", name="name_ru"),
        migrations.RemoveField(model_name="contact", name="name_en"),
        migrations.RemoveField(model_name="contact", name="name_ar"),
        migrations.RemoveField(model_name="contact", name="message_uz"),
        migrations.RemoveField(model_name="contact", name="message_ru"),
        migrations.RemoveField(model_name="contact", name="message_en"),
        migrations.RemoveField(model_name="contact", name="message_ar"),
        migrations.AlterField(
            model_name="project",
            name="client",
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="first_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="team",
            name="last_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(),
        ),
    ]
