from django.test import SimpleTestCase, TestCase
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Article

def user_args():
    return dict(username="TESTER", email="test@test.us", password="secret")


def test_user():
    return get_user_model().objects.create_user(**user_args())

# Create your tests here.
class HeroAppTest(TestCase):
    
    def test_django(self):
        page = "https://jellyfish-app-w75km.ondigitalocean.app/"
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)
        
class ArticleDataTest(TestCase):
    def test_data_model(self):

        # Add two articles
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title="Title 1", body="Body")
        Article.objects.create(title="Title 2", body="Body")
        self.assertEqual(len(Article.objects.all()), 2)

        # Check the details
        a = Article.objects.get(pk=2)
        self.assertEqual(a.title, "Title 2")

        # Edit the record
        a.title = "New Title"
        a.save()
        self.assertEqual(a.title, "New Title")

        # Delete a record
        a.delete()
        self.assertEqual(len(Article.objects.all()), 1)