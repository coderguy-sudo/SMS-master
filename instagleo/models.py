from django.db import models


class AbstractBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(AbstractBaseModel):
    name = models.CharField(max_length=256)
    course_no = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.name)


class Student(AbstractBaseModel):
    name = models.CharField(max_length=256)
    roll_no = models.CharField(max_length=256)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    marks = models.JSONField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
