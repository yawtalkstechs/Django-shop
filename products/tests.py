# products/tests.py
from django.test import TestCase
from .models import Category, Product
from company.models import Company
from django.contrib.auth.models import User

class ProductModelTest(TestCase):
    def setUp(self):
        # Create a company and a user associated with that company
        self.company = Company.objects.create(
            name='Test Company',
            registration_date='2023-01-01',
            address='Test Address',
            phone='123-456-7890',
            email='test@example.com',
            logo_url='http://www.testcompany.com/logo.png',
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.user.company = self.company
        self.user.save()

        # Create a category
        self.category = Category.objects.create(name='Test Category')

        # Create a product
        self.product = Product.objects.create(
            company=self.company,
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='Test description',
            price=19.99,
            stock_quantity=100,
            image_url='http://www.testproduct.com/image.png',
            available=True,
        )

    def test_product_creation(self):
        """Test the creation of a product."""
        self.assertEqual(self.product.__str__(), 'Test Product')
        self.assertEqual(self.product.company, self.company)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.slug, 'test-product')
        self.assertEqual(self.product.description, 'Test description')
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.stock_quantity, 100)
        self.assertEqual(self.product.image_url, 'http://www.testproduct.com/image.png')
        self.assertTrue(self.product.available)
        self.assertIsNotNone(self.product.created)
        self.assertIsNotNone(self.product.updated)
