from faker import Faker

from data.data import Customer

faker_en = Faker('En')
Faker.seed()


def generate_first_name(post_code: str):
    # Преобразуем число в строку для доступа к отдельным цифрам
    post_code_str = str(post_code)
    # Разбиваем строку на двузначные цифры
    digits = [int(post_code_str[i:i + 2]) for i in range(0, 10, 2)]
    # Преобразуем каждую цифру в соответствующую букву алфавита
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = [alphabet[digit % 26] for digit in digits]
    # Объединяем буквы в одну строку
    result = ''.join(letters)
    return result


def get_customer():
    post_code = faker_en.random_number(digits=10)
    first_name = generate_first_name(post_code)
    last_name = faker_en.last_name()
    yield Customer(first_name=first_name, last_name=last_name, post_code=post_code)
