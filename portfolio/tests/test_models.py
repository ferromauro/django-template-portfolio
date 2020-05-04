from django.test import TestCase
from model_bakery import baker
from portfolio.models import Project, TagProject
# Project item contains title, description, image, tags

class ProjectTestCase(TestCase):
    def setUp(self):
        self.models = baker.make(Project)

    def test_project_str(self):
        self.assertEqual(self.models.__str__(), str(self.models))        

class TagProjectTestCase(TestCase):
    def setUp(self):
        self.models = baker.make(TagProject)

    def test_tag_project_str(self):
        self.assertEqual(self.models.__str__(), str(self.models))        
