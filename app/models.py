from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ManyToManyField(Category, related_name="projects")
    link = models.URLField(blank=True)
    client = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    image = models.ImageField(upload_to="projects/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")

    def __str__(self) -> str:
        return f"Image for {self.project}"


class AboutUs(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="about/")

    def __str__(self) -> str:
        return "About Us"


class Profession(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to="team/")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profession = models.ForeignKey(
        Profession, on_delete=models.PROTECT, related_name="team_members"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="contacts")
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"


class Comment(models.Model):
    text = models.TextField()
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to="comments/")

    def __str__(self) -> str:
        return f"{self.username}: {self.text[:30]}"
