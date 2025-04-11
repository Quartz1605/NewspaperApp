from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class UserManagersTests(TestCase):
  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(
      username="test",
      email="test@gmail.com",
      password="test"
    )

    self.assertEqual(user.username,"test")
    self.assertEqual(user.email,"test@gmail.com")
    self.assertFalse(user.is_staff)
    self.assertTrue(user.is_active)

  def test_create_superuser(self):
    
    User = get_user_model()
    superuser = User.objects.create_superuser(
        username="super",
        email="super@gmail.com",
        password="superpass"
      )

    self.assertEqual(superuser.username,"super")
     
    self.assertTrue(superuser.is_staff)
    self.assertTrue(superuser.is_active)
    self.assertTrue(superuser.is_superuser)

class SignupPageTests(TestCase):
  def test_url_exists_at_location(self):
    response = self.client.get("/accounts/signup/")
    self.assertEqual(response.status_code,200)

  def test_signup_view(self):
    response = self.client.get(reverse("signup"))
    self.assertTemplateUsed(response,"registration/signup.html")
    self.assertEqual(response.status_code,200)

  def test_signup_form(self):
    response = self.client.post(
      reverse("signup"),{
        "username" :  "testuser",
        "email" : "user@gmail.com",
        "password1" : "rocket@123",
        "password2" : "rocket@123",
        
      }
    )
    self.assertEqual(get_user_model().objects.all().count(),1)
    



