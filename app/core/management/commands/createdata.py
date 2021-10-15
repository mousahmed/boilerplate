from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from members.models.members import Member
from members.models.services import Service
from members.models.countries import City
from django.template.defaultfilters import slugify
import random
from django_countries import countries
from members.models.countries import City
import os
import csv


module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'members_city.csv')


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username='admin')
        except:
            user = User.objects.create_superuser(
                username='admin',
                email='admin@website.com',
                password='testpass123'
            )
        fake = Faker()

        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = City.objects.get_or_create(
                    name=row[3],
                    user=user,
                    country='EG'
                )

        member_obj = Member.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            mobile=fake.unique.phone_number(),
            address=fake.address(),
            birthday=fake.date_of_birth(),
            user=user,
            city=City.objects.filter(name='New Cairo').first(),
            job="Engineer",
            marital_status="S",
            gender="F",
            height='175'
        )
        # for _ in range(10):
        #     membership_obj = Membership.objects.create(
        #         name=fake.word(),
        #         type=random.choice(['Clinic', 'Online']),
        #         period=random.randint(1, 12),
        #         sessions=random.randint(12, 120),
        #         price=random.randint(1000, 5000),
        #         user=user
