from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="title_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="description_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="description_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="description_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="description_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="client_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="client_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="client_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="client_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="text_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="text_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="text_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="text_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="profession",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="profession",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="profession",
            name="title_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="profession",
            name="title_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="first_name_uz",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="first_name_ru",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="first_name_en",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="first_name_ar",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="last_name_uz",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="last_name_ru",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="last_name_en",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="team",
            name="last_name_ar",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="name_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="name_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="description_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="description_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="description_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="service",
            name="description_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="name_en",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="name_ar",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="message_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="message_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="message_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="message_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="text_uz",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="text_ru",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="text_en",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="text_ar",
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="username_uz",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="username_ru",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="username_en",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="username_ar",
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
