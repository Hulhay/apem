import requests as r
from config.config import get_base_url
from assertpy import assert_that
from auth_helper import *

def test_register():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(200)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(200)
    assert_that(resp['meta']['message']).is_equal_to('success!')

def test_register_empty_name():
    base_url = get_base_url()

    name = ''
    email = get_email(name)
    password = get_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('name cannot be empty')

def test_register_empty_email():
    base_url = get_base_url()

    name = get_name()
    email = ''
    password = get_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('email cannot be empty')

def test_register_invalid_email():
    base_url = get_base_url()

    name = get_name()
    email = get_invalid_email()
    password = get_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('invalid email format')

def test_register_email_already_exists():
    base_url = get_base_url()

    name = get_name()
    email = get_email_exists()
    password = get_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('email already exists')

def test_register_empty_password():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = ''
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('password cannot be empty')

def test_register_short_password():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_short_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('password must have a minimum of 8 characters')

def test_register_invalid_password():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_invalid_password()
    phone_number = get_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('password must contain and contain only letters and numbers')

def test_register_empty_phone_number():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_password()
    phone_number = ''

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('phone number cannot be empty')

def test_register_invalid_phone_number():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_password()
    phone_number = get_invalid_phone_number()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('invalid phone number format')

def test_register_phone_number_already_exists():
    base_url = get_base_url()

    name = get_name()
    email = get_email(name)
    password = get_password()
    phone_number = get_phone_number_exists()

    body = get_payload(name, email, password, phone_number)

    response = r.post(f'{base_url}/api/v1/auth/register', json=body)
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(422)

    # Check meta
    assert_that(resp['meta']['code']).is_equal_to(422)
    assert_that(resp['meta']['message']).is_equal_to('phone number already exists')