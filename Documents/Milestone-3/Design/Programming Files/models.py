from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    
    def __str__(self):
        return self.user.username

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_photos', blank=True)

    def __str__(self):
        return f"Photo by {self.user.username}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.photo}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on {self.photo}"
