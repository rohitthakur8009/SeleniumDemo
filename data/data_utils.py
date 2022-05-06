import random

USERNAME_FORMAT = 'test_user_{}'


def generate_unique_username():
    return USERNAME_FORMAT.format(random.randint(10000, 1000000))
