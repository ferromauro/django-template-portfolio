from django.test import TestCase
from model_bakery import baker
from portfolio.models import Project
# Project item contains title, description, image, tags

class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = baker.make(Project)

    def test_project_str(self):
        pass        