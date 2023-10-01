from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
from django.shortcuts import get_object_or_404
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request, 'homepage/home.html', {'images': images})

def profile(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'homepage/profile.html', {'form': form})

def image_display(request):
    images = Image.objects.all().order_by('-id')  # Ordering by id in descending order to get the latest uploads first
    return render(request, 'your_template_name.html', {'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('home')