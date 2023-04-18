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

    name = models.CharField(("name"), max_length=100)
    email = models.EmailField(("email"), max_length=254)
    topic = models.CharField(("topic"), max_length=100)
    text = models.TextField(("text"))
    created = models.DateTimeField(("created"), auto_now_add=True)

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
    url = models.CharField(("url"), max_length=100, blank=True)

    class Meta:
        verbose_name = ("Projects")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return self.title


class BotUsers(models.Model):

    user_id = models.IntegerField(("user_id"))
    username = models.CharField(("username"), max_length=100)
    created = models.DateTimeField(("created"), auto_now_add=True)

    class Meta:
        verbose_name = ("BotUsers")
        verbose_name_plural = ("BotUsers")

    def __str__(self):
        return self.username


class ProjectsDecription(models.Model):

    text = models.TextField(("text"))

    class Meta:
        verbose_name = ("ProjectsDecription")
        verbose_name_plural = ("ProjectsDecriptions")

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse("ProjectsDecription_detail", kwargs={"pk": self.pk})


