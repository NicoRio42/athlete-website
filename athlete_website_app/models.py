from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class HeadBanner(models.Model):
    content = MarkdownxField()
    image = models.ImageField(upload_to='head-banner-images/')
    
    # Property that returns the markdown instead
    @property
    def content_markdown(self):
        return markdownify(self.content)


class HeadText(models.Model):
    content = MarkdownxField()

    @property
    def content_markdown(self):
        return markdownify(self.content)


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    short_content = MarkdownxField()
    content = MarkdownxField()
    image = models.ImageField(upload_to='articles-images/')

    @property
    def content_markdown(self):
        return markdownify(self.content)

    @property
    def short_content_markdown(self):
        return markdownify(self.short_content)


class SponsorBanner(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()

    @property
    def content_markdown(self):
        return markdownify(self.content)


class Sponsor(models.Model):
    title = models.CharField(max_length=200)
    description = MarkdownxField()
    url = models.URLField()
    image = models.ImageField(upload_to='sponsors-logos/')

    @property
    def description_markdown(self):
        return markdownify(self.description)