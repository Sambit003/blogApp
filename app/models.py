from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

'''
the below class is the model for the tag and it has the following fields:
name: the name of the tag
description: the description of the tag
slug: the slug of the tag
'''


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
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


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True)

    is_featured = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    bookmarks = models.ManyToManyField(User, related_name='bookmarks', blank=True, default=None)

    likes = models.ManyToManyField(User, related_name='likes', blank=True, default=None)

    def total_likes(self):
        return self.likes.count()


'''
the below class is the model for the comments and it has the following fields:
content: the content of the comment
date: the date and time the comment was posted
name: the name of the person who posted the comment
email: the email of the person who posted the comment
website: the website of the person who posted the comment
post: the post the comment was posted on
author: the author of the comment
parent: the parent comment of the comment (if it is a reply)
'''


class Comments(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')


'''
the below class is the model for the subscribe and it has the following fields:
email: the email of the person who subscribed
date: the date and time the person subscribed
'''


class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField(blank=True, null=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.first_name


class WebsiteMeta(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    about = models.TextField(max_length=5000)
