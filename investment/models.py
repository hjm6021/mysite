from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    description = models.CharField("DESCRIPTION", max_length=100, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    # content = models.TextField("CONTENT")
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        db_table = "investment_posts"
        ordering = ("-modify_dt",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("study:detail", args=(self.category_id.slug, self.pk))
    
class Category(models.Model):
    name = models.CharField(verbose_name="NAME", max_length=50)
    slug = models.SlugField("SLUG", unique=True, allow_unicode=True)
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)

    def __str__(self):
        return self.name