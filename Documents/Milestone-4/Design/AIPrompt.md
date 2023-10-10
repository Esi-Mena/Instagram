# AiPrompt Mileston-4
I asked chat gpt to "Create a design pattern to define the Django Data Model" and this is what it instructed me to do.

To define a Django data model for the given scenario, where we have a Student model with fields user, course, github, server, and email, you can use the Django Model design pattern. In Django, models are typically defined in a Python class that inherits from django.db.models.Model

![image](https://github.com/Esi-Mena/Instagram/assets/89554958/f0edb69d-3f8e-4c27-89e5-0cc45a2b0821)

It then explains the steps and why

1. We import the necessary modules from Django.
2. We create a Student model that inherits from models.Model.
3. We define fields for user, course, github, server, and email.

-user is linked to the built-in User model using a OneToOneField, indicating a one-to-one relationship between a Student and a User. This allows you to associate a User with a Student record.

-course is a character field for the course information.

-github is a URL field for the GitHub profile, and it's optional (blank=True, null=True) because not all students may have a GitHub profile.

-server is a character field for server information, and it's also optional.

-email is an email field for the student's email address.

4. We define a __str__ method to provide a human-readable representation of a Student object. In this case, it returns the username of the associated User object, but you can customize it as needed.
