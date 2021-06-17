from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Book, Author

# Create your tests here.


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Mohammad", email="mohammad@gmail.com", password="password"
        )
        
        self.author = Author.objects.create(
            name = 'William Shakespear',
            language = 'English'
        )
        self.book = Book.objects.create(
            title="hamlet",
            author=self.author,
            seller=self.user,
            publish_date = "1980-01-01",
            isbn = "12456287451123"

        )


    def test_string_representation(self):
        self.assertEqual(str(self.book), "hamlet")

    def test_book_content(self):
        self.assertEqual(f"{self.book.title}", "hamlet")
        self.assertEqual(f"{self.book.author}", "William Shakespear")
        self.assertEqual(f"{self.book.seller }", "mohammad@gmail.com")
        self.assertEqual(f"{self.book.publish_date }", "1980-01-01")
        self.assertEqual(f"{self.book.isbn }", "12456287451123")
        




    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hamlet")
        self.assertTemplateUsed(response, "bookshop/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(reverse("book_detail", args="1"))
        no_response = self.client.get("/10/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Title: hamlet")
        self.assertTemplateUsed(response, "bookshop/book_detail.html")

    def test_book_create_view(self):
        response = self.client.post(
            reverse("book_create"),
            {
                "title": "macbeth",
                "author": self.author,
                "seller": self.user.id,
                "publish_date": "1606-01-01",
                "isbn": 1123,
            }, follow=True
        )
        redirect_url = reverse('book_detail', args='1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookshop/book_create.html")
    
    def test_book_delete_view(self):
        response = self.client.get(reverse("book_delete", args="1"))
        self.assertEqual(response.status_code, 200)