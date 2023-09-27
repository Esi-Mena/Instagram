from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo, Comment, UserProfile
from .forms import PhotoForm, CommentForm

@login_required
def home(request):
    # Display the user's home feed with photos from followed users
    following_users = request.user.userprofile.followers.all()
    photos = Photo.objects.filter(user__in=following_users).order_by('-created_at')
    return render(request, 'home.html', {'photos': photos})

@login_required
def upload_photo(request):
    # Allow users to upload photos
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Photo uploaded successfully.')
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

@login_required
def photo_detail(request, photo_id):
    # Display the details of a single photo, including comments and likes
    photo = get_object_or_404(Photo, pk=photo_id)
    comments = Comment.objects.filter(photo=photo)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.photo = photo
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('photo_detail', photo_id=photo_id)
    else:
        form = CommentForm()
    return render(request, 'photo_detail.html', {'photo': photo, 'comments': comments, 'form': form})

@login_required
def user_profile(request, username):
    # Display a user's profile and their uploaded photos
    user = get_object_or_404(UserProfile, username=username)
    photos = Photo.objects.filter(user=user).order_by('-created_at')
    return render(request, 'user_profile.html', {'user': user, 'photos': photos})

@login_required
def like_photo(request, photo_id):
    # Allow users to like/unlike photos
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    return redirect('photo_detail', photo_id=photo_id)

@login_required
def follow_user(request, username):
    # Allow users to follow/unfollow other users
    user_to_follow = get_object_or_404(UserProfile, username=username)
    user_profile = request.user.userprofile
    if user_to_follow == request.user:
        messages.warning(request, 'You cannot follow yourself.')
    elif user_to_follow in user_profile.followers.all():
        user_profile.followers.remove(user_to_follow)
    else:
        user_profile.followers.add(user_to_follow)
    return redirect('user_profile', username=username)
