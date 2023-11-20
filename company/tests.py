# company/tests.py
from datetime import date
from django.test import TestCase
from .models import Company
from django.contrib.auth.models import User

class CompanyModelTest(TestCase):
    def setUp(self):
        # Create a user associated with the company
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.company = Company.objects.create(
            name='Test Company',
            registration_date=date.today(),
            address='Test Address',
            phone='123-456-7890',
            email='test@example.com',
            logo_url='http://www.testcompany.com/logo.png',
        )
        self.user.company = self.company
        self.user.save()

    def test_company_creation(self):
        """Test the creation of a company."""
        self.assertEqual(self.company.__str__(), 'Test Company')
        self.assertEqual(self.company.name, 'Test Company')
        self.assertEqual(self.company.registration_date, date.today())
        self.assertEqual(self.company.address, 'Test Address')
        self.assertEqual(self.company.phone, '123-456-7890')
        self.assertEqual(self.company.email, 'test@example.com')
        self.assertEqual(self.company.logo_url, 'http://www.testcompany.com/logo.png')

    def test_company_user_association(self):
        """Test the association of a user with a company."""
        self.assertEqual(self.user.company, self.company)
