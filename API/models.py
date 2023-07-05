from django.db import models
from django.utils.timezone import now
from rest_framework.authtoken.admin import User


class HomeModel(models.Model):
    HomeImage = models.ImageField(upload_to="images")
    safeDesc = models.TextField()
    doctorsAtWork = models.IntegerField(default=0)
    SatisfiedPatient = models.IntegerField(default=0)
    BedFacility = models.IntegerField(default=0)
    Hospitals = models.IntegerField(default=0)


class ServicesModel(models.Model):
    ServiceName = models.CharField(max_length=200)
    careDesc = models.TextField()

    def __str__(self):
        return self.ServiceName


class AboutModel(models.Model):
    AboutUsImage = models.ImageField(upload_to="images")
    aboutUsDesc = models.TextField()


class DoctorsModel(models.Model):
    DoctorImage = models.ImageField(upload_to="images")
    DoctorName = models.CharField(max_length=300)
    DoctorExpertize = models.CharField(max_length=300)

    def __str__(self):
        return self.DoctorName + self.DoctorExpertize


class BookModel(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.name


class ReviewModel(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField()
    image = models.ImageField(upload_to='images', null=None)

    def __str__(self):
        return self.name


class commentModel(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    Times = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13]


class ContactModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField(default=0)
    message = models.TextField()

    def __str__(self):
        return self.first_name
