from django.db import models
from django.utils.text import slugify

'''
the below class is the model for the tag and it has the following fields:
name: the name of the tag
description: the description of the tag
slug: the slug of the tag
'''
class Tag (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
'''
the below class is the model for the blog post and it has the following fields:
title: the title of the post
content: the content of the post
last_modified: the date and time the post was last modified
slug: the slug of the post
image: the image of the post
'''
class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null = True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag , blank=True, related_name='post')


    def __str__(self):
        return self.title