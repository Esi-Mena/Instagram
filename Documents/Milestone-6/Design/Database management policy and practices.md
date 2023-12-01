
# Documentation: Defining database management policy and practices 

## Overview
This documentation details the implementation of a key database management policy focusing on Data Integrity and Validation in the Django Instagram clone app. The goal is to ensure the reliability and consistency of the data within our application.

## Data Integrity and Validation Implementations

### 1. `UserProfile` Model Validation
- **Objective**: Maintain the integrity of user profile information.
- **Details**:
  - Bio length limited to 500 characters.
  - Website URLs are validated for correct format.

    ```python
    from django.core.validators import URLValidator, MaxLengthValidator

    class UserProfile(models.Model):
        bio = models.TextField(max_length=500, validators=[MaxLengthValidator(500)])
        website = models.URLField(blank=True, validators=[URLValidator()])
        # Other fields remain unchanged
    ```

### 2. `Photo` Model Validation
- **Objective**: Ensure appropriate upload of either a photo or a video.
- **Details**:
  - Custom clean method to validate that only one of the image or video fields is populated.

    ```python
    class Photo(models.Model):
        image = models.ImageField(upload_to='photos/', null=True, blank=True)
        video = models.FileField(upload_to='videos/', null=True, blank=True)

        def clean(self):
            if self.image and self.video:
                raise ValidationError('Either an image or a video can be uploaded, not both.')
            if not self.image and not self.video:
                raise ValidationError('Either an image or a video must be uploaded.')
    ```

### 3. `Comment` Model Validation
- **Objective**: Prevent empty comments.
- **Details**:
  - Validation to ensure the comment text is not empty.

    ```python
    class Comment(models.Model):
        text = models.TextField(validators=[MaxLengthValidator(1000)])

        def clean(self):
            if not self.text.strip():
                raise ValidationError('Comment text cannot be empty.')
    ```

### 4. `Like` Model - Unique Together Constraint
- **Objective**: Prevent multiple likes on the same photo by a user.
- **Details**:
  - Unique together constraint on user and photo fields.

    ```python
    class Like(models.Model):
        class Meta:
            unique_together = ('user', 'photo',)
    ```

## Testing and Validation
- Rigorous testing was conducted post-implementation to ensure validations and constraints were enforced.
- Unit testing for each model's `clean` method and database constraints verification were performed.

## Conclusion
Implementing the Data Integrity and Validation policy significantly enhances the robustness and reliability of our application. It ensures data consistency and adheres to defined business rules, contributing to the overall quality of the app.
