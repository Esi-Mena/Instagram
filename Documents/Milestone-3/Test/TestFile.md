from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Photo, Comment, UserProfile, Like, User


class YourAppViewsTestCase(TestCase):


    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
#PASSING

    def test_successful_signup(self):
        # Setup
        user_count = User.objects.count()  # Count users before signup
        signup_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        # Test
        response = self.client.post(reverse('signup'), data=signup_data)
        # Check
        self.assertRedirects(response, reverse('home'))  # After signup, user should be redirected to home
        self.assertEqual(User.objects.count(), user_count + 1)  # User count should increase by 1

#PASSING

    def test_successful_comment_on_photo(self):
        # Setup
        self.client.login(username='testuser', password='testpassword')
        # Create a test photo
        photo = Photo.objects.create(user=self.user, image='path_to_some_test_image.jpg', caption='Test Caption')
        comment_count = Comment.objects.filter(photo=photo).count()  # Count comments before new comment
        comment_data = {
            'text': 'Test Comment',
        }
        # Test
        response = self.client.post(reverse('photo_detail', kwargs={'photo_id': photo.id}), data=comment_data)
        # Check
        self.assertRedirects(response, reverse('photo_detail', kwargs={'photo_id': photo.id}))  # After comment, user should be redirected to photo detail
        self.assertEqual(Comment.objects.filter(photo=photo).count(), comment_count + 1)  # Comment count for the photo should increase by 1

#PASSING

    def test_successful_photo_upload(self):
        self.client.login(username='testuser', password='testpassword')
        photo_count_before = Photo.objects.count()
    
        with open('test_data/test_image.jpg', 'rb') as photo_file:
         response = self.client.post(reverse('upload_photo'), {'image': photo_file, 'caption': 'Test Caption'})
    
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Photo.objects.count(), photo_count_before + 1)
#FAILLLING

    def test_edit_profile(self):
        self.client.login(username='testuser', password='testpassword')
    
        profile = UserProfile.objects.get(user=self.user)
        old_bio = profile.bio
    
        new_bio = "This is a new bio for testing."
        response = self.client.post(reverse('edit_profile'), {'bio': new_bio})
    
        profile.refresh_from_db()
        self.assertNotEqual(old_bio, profile.bio)
        self.assertEqual(profile.bio, new_bio)
        self.assertRedirects(response, reverse('user_profile', kwargs={'username': self.user.username}))

#FAILLLING

    def test_search_profiles(self):
    # Create two more test users
        User.objects.create_user(username='john', password='testpassword')
        User.objects.create_user(username='jane', password='testpassword')
    
        search_query = 'jo'
        response = self.client.get(reverse('search_profiles'), {'q': search_query})
    
        users_in_context = response.context['results']
        self.assertEqual(len(users_in_context), 2)
        self.assertTrue(any(user.username == 'john' for user in users_in_context))
        self.assertTrue(any(user.username == 'jane' for user in users_in_context))

#FAILLLING

    def test_follow_user(self):
    # Create another test user
        another_user = User.objects.create_user(username='anotheruser', password='testpassword')
        another_profile = UserProfile.objects.create(user=another_user)
    
        self.client.login(username='testuser', password='testpassword')
        followers_count_before = another_profile.followers.count()
    
        response = self.client.get(reverse('follow_user', kwargs={'username': another_user.username}))
    
        self.assertRedirects(response, reverse('user_profile', kwargs={'username': another_user.username}))
        self.assertEqual(another_profile.followers.count(), followers_count_before + 1)

#FAILLLING

    def test_like_photo(self):
        self.client.login(username='testuser', password='testpassword')
        # Create a test photo
        photo = Photo.objects.create(user=self.user, image='test_data/test_image.jpg', caption='Test Caption')
        like_count_before = Like.objects.filter(photo=photo).count()
        
        response = self.client.get(reverse('like_photo', kwargs={'photo_id': photo.id}))
   
        self.assertRedirects(response, reverse('photo_detail', kwargs={'photo_id': photo.id}))
        self.assertEqual(Like.objects.filter(photo=photo).count(), like_count_before + 1)

#PASSING

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

  #PASSING   
  
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

  #PASSING  
  
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

  #FAILLLING  
  
    def test_authenticated_user_redirect_home(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('signup'))
        # Since the user is logged in, they should be redirected to the home page
        self.assertRedirects(response, reverse('home'))

#FAILLLING

    def test_authenticated_user_redirect_login(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('login'))
        # Since the user is logged in, they should be redirected to the home page
        self.assertRedirects(response, reverse('home'))

