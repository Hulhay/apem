from config.config import init_faker
from utils.contant import AUTH_CONSTANTS

fake = init_faker()

def get_name():
    return f'Oto {fake.name()}'

def get_email(name):
    return f'{name.replace(" ", "").lower()}@{AUTH_CONSTANTS["email_domain"]}'

def get_invalid_email():
    return AUTH_CONSTANTS['invalid_email']

def get_email_exists():
    return AUTH_CONSTANTS['email_exists']

def get_password():
    return AUTH_CONSTANTS['password']

def get_short_password():
    return AUTH_CONSTANTS['short_password']

def get_invalid_password():
    return AUTH_CONSTANTS['invalid_password']

def get_phone_number():
    phone_number = fake.msisdn()
    return f'08{phone_number[0:10]}'

def get_invalid_phone_number():
    phone_number = fake.msisdn()
    return f'62{phone_number}'

def get_phone_number_exists():
    return AUTH_CONSTANTS['phone_number_exits']

def get_payload(name, email, password, phone_number):
    return {
        'name': name,
        'email': email,
        'password': password,
        'phone_number': phone_number,
    }