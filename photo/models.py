from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    bio = models.CharField(max_length=350, null=True) 
    profile_pic = models.ImageField(upload_to='ProfilePicture/', null=True)
    # profile_avatar = models.ImageField(upload_to='AvatorPicture/', null=True)
    date = models.DateTimeField(auto_now_add=True, null= True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)

    @receiver(post_save, sender=User)
    def update_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


    def save_profile(self):
        self.save()
    
    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = User.objects.filter(username__icontains = name)
        return userprof

    
class Comments (models.Model):
    comment_post = models.CharField(max_length=150, null=True)
    author = models.ForeignKey('Profile',related_name='comment' , on_delete=models.CASCADE)
    commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['comment_post', 'author','commented_image']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def find_commentimage(cls,id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
	

class Image(models.Model):

    image = models.ImageField(upload_to ='pictsagram/',null=True)
    image_caption = models.CharField(max_length=700, null=True)
    tag_someone = models.CharField(max_length=50,blank=True, null=True)
    profile = models.ForeignKey(Profile, null = True,on_delete=models.CASCADE,related_name='image')
    image.user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True,related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null= True)
    # comment = models.ForeignKey(Comments, null=True ,on_delete=models.CASCADE)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def save_image(self):
        self.save()
    
    @classmethod
    def get_by_id(cls,id):
        image= Image.objects.get(user = id)
        return image

    @classmethod
    def get_images(cls, profile):
        image = Image.objects.filter(Profile__pk = profile)
        return image
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    @classmethod
    def find_image_id(cls, id):
        identity = Image.objects.get(pk=id)
        return identity



class Follow(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    follower = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __int__(self):
        return self.name

    def save_unfollower(self):
        self.save()

    def delete_unfollower(self):
        self.save()
    



