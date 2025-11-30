from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Authenticate user
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            description="Sample description",
            published_year=2020
        )

        self.list_url = reverse("book-list")   # For List/Create endpoint
        self.detail_url = reverse("book-detail", args=[self.book.id])  # For Retrieve/Update/Delete


    # -------------------------------------------------------
    # CREATE
    # -------------------------------------------------------
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author X",
            "description": "New description",
            "published_year": 2023
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")


    # -------------------------------------------------------
    # LIST
    # -------------------------------------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


    # -------------------------------------------------------
    # RETRIEVE
    # -------------------------------------------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)


    # -------------------------------------------------------
    # UPDATE (PUT)
    # -------------------------------------------------------
    def test_update_book(self):
        data = {"title": "Updated Book"}

        response = self.client.patch(self.detail_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")


    # -------------------------------------------------------
    # DELETE
    # -------------------------------------------------------
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())


    # -------------------------------------------------------
    # PERMISSIONS: UNAUTHENTICATED USER
    # -------------------------------------------------------
    def test_unauthenticated_user_cannot_create(self):
        client = APIClient()  # no login

        data = {"title": "Blocked Book"}

        response = client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # -------------------------------------------------------
    # SEARCH & FILTER
    # -------------------------------------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Test")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=title")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
