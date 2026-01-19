import json
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files import File

from app.models import AboutUs, Comment, Service


class Command(BaseCommand):
    help = "Import AboutUs, Comment and Service data from JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default="export_content.json",
            help="Path to JSON file (default: export_content.json)",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing data before import",
        )

    def handle(self, *args, **options):
        json_path = options["path"]

        if not os.path.exists(json_path):
            raise CommandError(f"JSON file not found: {json_path}")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if options["clear"]:
            self.stdout.write("Clearing existing data...")
            AboutUs.objects.all().delete()
            Comment.objects.all().delete()
            Service.objects.all().delete()

        # ---------- AboutUs ----------
        for item in data.get("about_us", []):
            obj = AboutUs.objects.create(
                text_uz=item["text_uz"],
                text_ru=item.get("text_ru"),
                text_en=item.get("text_en"),
                text_ar=item.get("text_ar"),
            )

            self._attach_image(obj, item.get("image"))

        # ---------- Comment ----------
        for item in data.get("comments", []):
            obj = Comment.objects.create(
                text_uz=item["text_uz"],
                text_ru=item.get("text_ru"),
                text_en=item.get("text_en"),
                text_ar=item.get("text_ar"),
                username_uz=item["username_uz"],
                username_ru=item.get("username_ru"),
                username_en=item.get("username_en"),
                username_ar=item.get("username_ar"),
            )

            self._attach_image(obj, item.get("image"))

        # ---------- Service ----------
        for item in data.get("services", []):
            Service.objects.create(
                name_uz=item["name_uz"],
                name_ru=item.get("name_ru"),
                name_en=item.get("name_en"),
                name_ar=item.get("name_ar"),
                description_uz=item.get("description_uz"),
                description_ru=item.get("description_ru"),
                description_en=item.get("description_en"),
                description_ar=item.get("description_ar"),
            )

        self.stdout.write(self.style.SUCCESS("Data successfully imported ✅"))

    def _attach_image(self, obj, image_path):
        """
        image_path example: /media/about/about1.jpg
        """
        if not image_path:
            return

        # убираем MEDIA_URL
        relative_path = image_path.replace(settings.MEDIA_URL, "").lstrip("/")
        full_path = os.path.join(settings.MEDIA_ROOT, relative_path)

        if not os.path.exists(full_path):
            self.stdout.write(
                self.style.WARNING(f"Image not found: {full_path}")
            )
            return

        with open(full_path, "rb") as f:
            obj.image.save(
                os.path.basename(full_path),
                File(f),
                save=True,
            )