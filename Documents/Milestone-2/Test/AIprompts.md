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


      ![image](https://github.com/Esi-Mena/Instagram/assets/89554958/48492adf-29aa-44f1-8663-fb794f1e1bda)

These test cases include checking if a student can be created with the expected attributes, if the "name" field respects its maximum length, and if the "email" field enforces uniqueness.

5.**Run Tests:**
To run your tests, use the following command:

**python manage.py test your_app_name**
Replace "your_app_name" with the name of your Django app where the Student model is defined.

6.Review Test Results:
Django will execute the tests and provide feedback on whether they pass or fail. Make any necessary adjustments to your code until all tests pass successfully.

By following these steps, you can create Django unit tests to ensure that your Student model functions correctly and adheres to your specified criteria.
