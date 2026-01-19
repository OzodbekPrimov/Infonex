import json
from django.core.management.base import BaseCommand
from django.conf import settings

from app.models import AboutUs, Comment, Service


class Command(BaseCommand):
    help = "Export AboutUs, Comment and Service data to JSON file"

    def handle(self, *args, **options):
        data = {
            "about_us": [],
            "comments": [],
            "services": [],
        }

        # ---------- AboutUs ----------
        for item in AboutUs.objects.all():
            data["about_us"].append({
                "text_uz": item.text_uz,
                "text_ru": item.text_ru,
                "text_en": item.text_en,
                "text_ar": item.text_ar,
                "image": item.image.url if item.image else None,
            })

        # ---------- Comment ----------
        for item in Comment.objects.all():
            data["comments"].append({
                "text_uz": item.text_uz,
                "text_ru": item.text_ru,
                "text_en": item.text_en,
                "text_ar": item.text_ar,
                "username_uz": item.username_uz,
                "username_ru": item.username_ru,
                "username_en": item.username_en,
                "username_ar": item.username_ar,
                "image": item.image.url if item.image else None,
            })

        # ---------- Service ----------
        for item in Service.objects.all():
            data["services"].append({
                "name_uz": item.name_uz,
                "name_ru": item.name_ru,
                "name_en": item.name_en,
                "name_ar": item.name_ar,
                "description_uz": item.description_uz,
                "description_ru": item.description_ru,
                "description_en": item.description_en,
                "description_ar": item.description_ar,
            })

        # ---------- Save JSON ----------
        output_path = settings.BASE_DIR / "export_content.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.stdout.write(
            self.style.SUCCESS(f"Data successfully exported to {output_path}")
        )
