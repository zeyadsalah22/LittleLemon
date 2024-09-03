
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=10, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=8, inventory=30)
        self.menu3 = Menu.objects.create(title="Salad", price=6, inventory=20)

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_data)