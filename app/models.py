from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=255, unique=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name_uz


class Service(models.Model):
    name_uz = models.CharField(max_length=255, unique=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)

    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name_uz} - {self.order}"


class Project(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    description_uz = models.TextField()
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name="projects")
    link = models.URLField(blank=True)
    client = models.CharField(max_length=255, blank=True)
    services = models.ManyToManyField(Service, related_name="projects", blank=True)

    year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title_uz


class ProjectImage(models.Model):
    image = models.ImageField(upload_to="projects/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    is_main=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Image for {self.project}"


class AboutUs(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField(blank=True, null=True)
    text_en = models.TextField(blank=True, null=True)
    text_ar = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="about/")

    def __str__(self) -> str:
        return "About Us"


class Profession(models.Model):
    title_uz = models.CharField(max_length=255, unique=True)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.title_uz


class Team(models.Model):
    image = models.ImageField(upload_to="team/")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profession = models.ForeignKey(
        Profession, on_delete=models.PROTECT, related_name="team_members"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"




class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="contacts")
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"


class Comment(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField(blank=True, null=True)
    text_en = models.TextField(blank=True, null=True)
    text_ar = models.TextField(blank=True, null=True)
    username_uz = models.CharField(max_length=150)
    username_ru = models.CharField(max_length=150, blank=True, null=True)
    username_en = models.CharField(max_length=150, blank=True, null=True)
    username_ar = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to="comments/")

    def __str__(self) -> str:
        return f"{self.username_uz}: {self.text_uz[:30]}"


class FAQ(models.Model):
    question_uz=models.CharField(max_length=255)
    question_en=models.CharField(max_length=255)
    question_ar=models.CharField(max_length=255)
    question_ru=models.CharField(max_length=255)
    answer_uz=models.CharField(max_length=255)
    answer_en=models.CharField(max_length=255)
    answer_ar=models.CharField(max_length=255)
    answer_ru=models.CharField(max_length=255)
