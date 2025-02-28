from faker import Faker

fake = Faker()
full_name = fake.first_name() + " " + fake.last_name()
TEST_CARD = {
        'fullname': full_name,
        'number': '4111111111111111',
        'exp': '12/27',
        'cvv': '123',
        'zip': '11111'
    }

