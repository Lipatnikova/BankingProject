from faker import Faker
from data.data import Customer
import random

faker_en = Faker('En')
Faker.seed()


def get_customer():
    yield Customer(
        last_name=faker_en.last_name()
    )


def generate_post_code():
    return str(random.randint(10 ** 9, 10 ** 10 - 1))
