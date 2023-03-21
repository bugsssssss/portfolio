from django.db import models

# Create your models here.


class About(models.Model):

    picture = models.ImageField(("picture"), upload_to='profile', null=True)
    skills = models.TextField(("skills"))
    experience = models.TextField(("experience"))
    additional = models.TextField(("additional"))

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return self.experience[:10]


class Callback(models.Model):

    email = models.EmailField(("email"), max_length=254)
    topic = models.CharField(("topic"), max_length=100)
    text = models.TextField(("text"))

    class Meta:
        verbose_name = ("Callback")
        verbose_name_plural = ("Callbacks")

    def __str__(self):
        return self.email + ' ' + self.topic


class Projects(models.Model):

    backround = models.ImageField(
        ("background"), upload_to='projects/background')
    title = models.CharField(("title"), max_length=100)
    description = models.TextField(("description"))
    quote = models.CharField(("quote"), max_length=150, blank=True)
    author = models.CharField(("author"), max_length=50, blank=True)
    picture1 = models.ImageField(("picture1"), upload_to='projects/photo')
    picture2 = models.ImageField(("picture2"), upload_to='projects/photo')
    cover = models.ImageField(("cover"), upload_to='projects/cover')
    url = models.CharField(("url"), max_length=100)

    class Meta:
        verbose_name = ("Projects")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title
