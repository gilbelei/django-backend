# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_curso():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'short_description': fake.sentence(nb_words=12),
        'time_description': fake.random_number(digits=2, fix_len=True),
        'hours_description': fake.random_number(digits=4, fix_len=True),
        'long_description': fake.text(3000),
        'category': {
            'name': fake.text(20),
            'type': fake.text(10),
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_curso())
