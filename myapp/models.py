from django.db import models

# Create your models here.

#  About Section
class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.name

#  Skill Section
class Skill(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.percentage}%"

#  Project Section
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

#  Education Section
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.degree

#  Experience Section
class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

#  Contact Section
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"

