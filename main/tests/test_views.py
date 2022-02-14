from django.test import TestCase
from django.shortcuts import reverse

class IndexPageTest(TestCase):
    
    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
    
    def test_index_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "main/index.html")


class FavoritesPageTest(TestCase):
    
    def test_favorites_page(self):
        response = self.client.get(reverse("favorite"), follow=True)
        self.assertEqual(response.status_code, 200)

