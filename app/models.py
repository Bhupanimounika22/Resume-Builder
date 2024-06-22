from django.db import models


class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin_profile = models.URLField()
    address = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    schooling = models.CharField(max_length=255)
    schooling_duration = models.CharField(max_length=100)
    intermediate = models.CharField(max_length=255)
    intermediate_duration = models.CharField(max_length=100)
    btech = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    btech_duration = models.CharField(max_length=100)

    def __str__(self):
        return f"Education for {self.resume.first_name} {self.resume.last_name}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.resume.first_name} {self.resume.last_name}"

class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Certificate for {self.resume.first_name} {self.resume.last_name}"

class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.language} - {self.resume.first_name} {self.resume.last_name}"

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Work Experience at {self.company_name} - {self.resume.first_name} {self.resume.last_name}"
