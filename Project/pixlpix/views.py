from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Photo, Comment, Like, User
from .forms import PhotoUploadForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import PhotoUploadForm, CommentForm, LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from .forms import PhotoForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create a new user account
            user = form.save()

            # Log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Replace 'home' with the name of your home view

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    # Retrieve photos and other data here
    photos = Photo.objects.all()  # Replace with actual query
    context = {'photos': photos}
    return render(request, 'home.html', context)

@login_required
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'user_profile.html', context)

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded photo and associate it with the current user
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('home')
    else:
        form = PhotoUploadForm()
    
    context = {'form': form}
    return render(request, 'upload_photo.html', context)

@login_required
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    comments = Comment.objects.filter(photo=photo)
    is_liked = Like.objects.filter(user=request.user, photo=photo).exists()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Save the comment and associate it with the current user and photo
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.photo = photo
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('photo_detail', photo_id=photo_id)
    else:
        comment_form = CommentForm()
    
    context = {'photo': photo, 'comments': comments, 'comment_form': comment_form, 'is_liked': is_liked}
    return render(request, 'photo_detail.html', context)


@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    # Add logic to handle liking the photo (e.g., add the user to the liked_photos ManyToMany field)

    # Redirect back to the photo detail page or another appropriate URL
    return redirect('photo_detail', photo_id=photo_id)

@login_required
def unlike_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    # Add logic to handle unliking the photo (e.g., remove the user from the liked_photos ManyToMany field)

    # Redirect back to the photo detail page or another appropriate URL
    return redirect('photo_detail', photo_id=photo_id)

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(UserProfile, user__username=username)

    # Add logic to handle following the user (e.g., add the user_to_follow to the followers ManyToMany field)

    # Redirect back to the user's profile page or another appropriate URL
    return redirect('user_profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(UserProfile, user__username=username)

    # Add logic to handle unfollowing the user (e.g., remove the user_to_unfollow from the followers ManyToMany field)

    # Redirect back to the user's profile page or another appropriate URL
    return redirect('user_profile', username=username)

def login_view(request):

    if request.method == 'POST':
        # Get the username and password from the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html', {'form': LoginForm})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def landing_view(request):
    return render(request, 'landing.html')

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})



def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo_update.html', {'form': form, 'photo': photo})

def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('photo_list')
    return render(request, 'photo_delete.html', {'photo': photo})