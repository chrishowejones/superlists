from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Home page tests
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve ('/')
        self.assertEquals(found.func, home_page)
