import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post modeli için gerekli alanlar tanımlanmıştır. """
    title = models.CharField(max_length=160, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    source = models.URLField(null=True, blank=True, default=None, verbose_name="Kaynak")
    image = models.ImageField(null=True, blank=True, default=None, verbose_name="Resim")
    liked = models.IntegerField(default=0)
    reported = models.PositiveIntegerField(default=0)
    categories = models.ForeignKey("Category", verbose_name="Kategori")
    tags = models.ManyToManyField("Tags")
    read = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=160, blank=True, unique=True)
    hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    featured_until = models.DateTimeField(default=None, blank=True, null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{}".format(self.title)


class Category(models.Model):
    """ Kategori modeli için gerekli tanımlamalar yapılmıştır """
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    super_parent = models.ForeignKey("self", blank=True, null=True, related_name="super_children")
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    color = models.CharField(max_length=6, blank=True, null=True, default=None)
    icon = models.CharField(max_length=150, blank=True, null=True, default=None)
    sub_level = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tags(models.Model):
    """ Etiketler modeli için gerekli tanımlamalar yapılmıştır """
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return "{}".format(self.tag)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Comments(models.Model):
    """ Yorumlar için gerekli tanımlamalar yapılmıştır """
    comment = models.TextField(verbose_name="Yorum")
    post = models.ForeignKey("Post")
    liked_count = models.PositiveIntegerField(default=0)
    reported = models.PositiveSmallIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.datetime.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - {}".format(self.comment, self.user_email)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class UserLikes(models.Model):
    """ Haberde kullanıcaya ait beğeni modeli tanımlanmıştır. """
    user = models.ForeignKey(User)
    post = models.ForeignKey("Post")


class Reports(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey("Post")
    message = models.CharField(max_length=180)


@receiver(pre_save, sender=Post)
@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Tags)
def define_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        elif hasattr(sender, "title"):
            instance.slug = slugify(instance.title)
        elif hasattr(sender, "tag"):
            instance.slug = slugify(instance.tag)
        else:
            raise AttributeError("It needs name, tag or title to define slug")
    return instance
