from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Photo, Comment

class InstagramAppViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test photo
        self.photo = Photo.objects.create(
            user=self.user,
            image='path/to/test_image.jpg',
            caption='Test photo caption'
        )

        # Create a test comment
        self.comment = Comment.objects.create(
            user=self.user,
            photo=self.photo,
            text='Test comment text'
        )

    def test_home_view(self):
        # Test the home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_upload_photo_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Test the upload photo view
        response = self.client.get(reverse('upload_photo'))
        self.assertEqual(response.status_code, 200)

    def test_photo_detail_view(self):
        # Test the photo detail view
        response = self.client.get(reverse('photo_detail', args=[self.photo.id]))
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view(self):
        # Test the user profile view
        response = self.client.get(reverse('user_profile', args=['testuser']))
        self.assertEqual(response.status_code, 200)

    def test_like_photo_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Test the like photo view
        response = self.client.get(reverse('like_photo', args=[self.photo.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after liking

    def test_follow_user_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Test the follow user view
        response = self.client.get(reverse('follow_user', args=['testuser']))
        self.assertEqual(response.status_code, 302)  # Should redirect after following

    # Add more test cases as needed for other views

    def tearDown(self):
        # Clean up test data
        self.client.logout()
        self.photo.delete()
        self.comment.delete()
        self.user.delete()
