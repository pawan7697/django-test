from django.test import TestCase
from book.models import Book
from datetime import date 

# Create your tests here.

class BookTestCase(TestCase):
    def setUp(self):
        # Use the current date for published_date
        today = date.today()
        Book.objects.create(title="Django for Beginners", author="William S. Vincent", published_date=today)
        Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", published_date=today)

    def test_book_creation(self):
        """Test if books are created correctly"""
        book1 = Book.objects.get(title="Django for Beginners")
        book2 = Book.objects.get(title="Two Scoops of Django")
        
        self.assertEqual(book1.author, "William S. Vincent")
        # Now comparing with the current date
        self.assertEqual(book2.published_date, date.today())

    def test_string_representation(self):
        """Test the string representation of the book"""
        book = Book.objects.get(title="Django for Beginners")
        self.assertEqual(str(book), book.title)