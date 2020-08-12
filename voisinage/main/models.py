from django.conf import settings
from django.db import models


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    avatar = models.ImageField(upload_to='avatars/', default='')
    pseudo = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    location = models.CharField(max_length=100)

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,
                             on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        return self.pseudo


class Business(models.Model):
    class Meta:
        verbose_name_plural = 'businesses'

    name = models.CharField(max_length=50, unique=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


class EmergencyService(models.Model):
    name = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=2,
                                  choices=(('FD', 'Fire Department'),
                                           ('PS', 'Police Station'),
                                           ('HS', 'Hospital')))
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    email = models.EmailField()

    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


class Post(models.Model):
    image = models.ImageField(upload_to='uploads/', default='', blank=True)
    title = models.TextField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
