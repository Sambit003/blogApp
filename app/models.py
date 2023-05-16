from django.db import models

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


    def __str__(self):
        return self.title
