from django import forms
from .models import Photo, Comment

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

    def clean_image(self):
        # Add custom validation for image size, format, or other criteria if needed
        image = self.cleaned_data.get('image')
        if image:
            # Example: Check if the image size is within a certain limit
            if image.size > 10 * 1024 * 1024:  # 10MB
                raise forms.ValidationError('The image size should be less than 10MB.')
        return image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def clean_text(self):
        # Add custom validation for comment text if needed
        text = self.cleaned_data.get('text')
        if text:
            # Example: Check for profanity or offensive content
            if 'profanity_check_here' in text:
                raise forms.ValidationError('Please refrain from using offensive language.')
        return text
