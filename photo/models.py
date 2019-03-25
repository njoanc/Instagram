from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=350) 
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    profile_avatar = models.ImageField(upload_to='AvatorPicture/')
    date = models.DateTimeField(auto_now_add=True, null= True)  


   
    def __str__(self):
        return self.profile.user

class Image(models.Model):

    image = models.ImageField(upload_to ='pictsagram/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50,blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.image_caption


class Comments (models.Model):
    comment_post = models.CharField(max_length=150)
    author = models.ForeignKey('Profile',related_name='comment' , on_delete=models.CASCADE)
    commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
	

class Follow(models.Model):
	user = models.ForeignKey(Profile,null=True)
	follower = models.ForeignKey(User,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
	user = models.ForeignKey(Profile,null=True)
	follower = models.ForeignKey(User,null=True)

	def __int__(self):
		return self.name
    



