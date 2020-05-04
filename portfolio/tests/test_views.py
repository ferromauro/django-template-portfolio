from django.test import TestCase
from django.test import Client
from django.urls import reverse
from portfolio.models import Project
from model_bakery import baker

class TestListView(TestCase):
    def setUp(self):
        self.client = Client()
    def test_status_code(self):
        response = self.client.get(reverse('portfolio_list'))
        self.assertEqual(response.status_code, 200)


class TestDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.model = baker.make(Project)
    def test_status_code(self):
        pk_model = self.model.pk
        response = self.client.get(reverse('portfolio_detail', kwargs={'pk': pk_model}))
        self.assertEqual(response.status_code, 200)


class TestAboutPage(TestCase):
    def setUp(self):
        self.client = Client()
    def test_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class TestContactPage(TestCase):
    def setUp(self):
        self.client = Client()
    def test_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

# Main page display portfolio list

# Detail page display portfolio item

# Personal page with bio

# Contacts page 