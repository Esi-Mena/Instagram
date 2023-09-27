# Ai prompts Milestone2
I asked chat gpt to Create Django unit tests for Student records (name, email, ID).
These are the directions it gave me in order to do this:

1. **Set Up Your Django Project:**
Ensure you have a Django project set up with the necessary models and database tables. Make sure you have a "Student" model with fields for "name," "email," and "ID."

2.**Create a Test File:**
In your Django app directory, create a Python file for your unit tests. You can name it something like "test_models.py" or "test_student.py."

3.**Import Necessary Modules:**
In your test file, import the necessary modules for testing and your Student model.

**from django.test import TestCase
from .models import Student**

4.**Write Test Cases:**
Create test cases that validate different aspects of the Student model. Here's an example of how to test the "name," "email," and "ID" fields:

class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            ID="12345"
        )
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.email, "johndoe@example.com")
        self.assertEqual(student.ID, "12345")

    def test_student_name_max_length(self):
        student = Student.objects.create(
            name="A" * 101,  # This exceeds the maximum length
            email="johndoe@example.com",
            ID="12345"
        )
        self.assertGreater(len(student.name), 100)  # Ensure it's too long

    def test_student_email_unique(self):
        # Create a student with a unique email
        student1 = Student.objects.create(
            name="John Doe",
            email="unique@example.com",
            ID="12345"
        )
        # Try to create another student with the same email (should raise an error)
        with self.assertRaises(Exception):
            Student.objects.create(
                name="Jane Doe",
                email="unique@example.com",
                ID="54321"
            )

These test cases include checking if a student can be created with the expected attributes, if the "name" field respects its maximum length, and if the "email" field enforces uniqueness.

5.**Run Tests:**
To run your tests, use the following command:

**python manage.py test your_app_name**
Replace "your_app_name" with the name of your Django app where the Student model is defined.

6.Review Test Results:
Django will execute the tests and provide feedback on whether they pass or fail. Make any necessary adjustments to your code until all tests pass successfully.

By following these steps, you can create Django unit tests to ensure that your Student model functions correctly and adheres to your specified criteria.
