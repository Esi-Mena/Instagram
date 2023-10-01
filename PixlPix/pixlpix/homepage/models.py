from django.db import models
from PIL import Image as PilImage

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')  # Your image field

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = PilImage.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)