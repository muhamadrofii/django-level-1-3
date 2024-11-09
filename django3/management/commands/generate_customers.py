from django.core.management.base import BaseCommand
from django3.models import Customer
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake customers'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(50):  # Adjust the number of customers to generate
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()

            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )

        self.stdout.write(self.style.SUCCESS('Successfully created fake customers'))
