from faker import Faker

fake = Faker()
full_name = fake.name()
TEST_CARD = {
        'fullname': full_name,
        'number': '4111111111111111',
        'exp': '12/27',
        'cvv': '123',
        'zip': '11111'
    }

