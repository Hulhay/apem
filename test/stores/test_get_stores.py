import requests as r
from config.config import base_url
from assertpy import assert_that

def test_get_stores():
    response = r.get(f'{base_url}/api/v1/stores')
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(200)
    
    # Check meta
    assert_that(resp).contains('meta')
    assert_that(resp['meta']['code']).is_equal_to(200)
    assert_that(resp['meta']['message']).is_equal_to('success')
    assert_that(resp['meta']['pagination']).contains('page')
    assert_that(resp['meta']['pagination']['page']).is_greater_than_or_equal_to(1)

    # Check data
    assert_that(resp).contains('data')
    assert_that(len(resp['data'])).is_greater_than_or_equal_to(1)
    
    # Check data -> uuid
    assert_that(resp['data'][0]).contains('uuid')
    assert_that(resp['data'][0]['uuid']).is_not_empty()
    assert_that(resp['data'][0]['uuid']).matches(r'^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$')

    # Check data -> store_name
    assert_that(resp['data'][0]).contains('store_name')
    assert_that(resp['data'][0]['store_name']).is_not_empty()

    # Check data -> store_photo_url
    assert_that(resp['data'][0]).contains('store_photo_url')

    # Check data -> owner_uuid
    assert_that(resp['data'][0]).contains('owner_uuid')
    assert_that(resp['data'][0]['owner_uuid']).is_not_empty()
    assert_that(resp['data'][0]['owner_uuid']).matches(r'^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$')

    # Check data -> owner_name
    assert_that(resp['data'][0]).contains('owner_name')
    assert_that(resp['data'][0]['owner_name']).is_not_empty()

    # Check data -> phone_number
    assert_that(resp['data'][0]).contains('owner_phone_number')
    assert_that(resp['data'][0]['owner_phone_number']).is_not_empty()
    assert_that(resp['data'][0]['owner_phone_number']).matches(r'^0\d+$')

def test_get_stores_with_valid_filter_keyword():
    keyword = 'ayam'

    response = r.get(f'{base_url}/api/v1/stores?keyword={keyword}')
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(200)

    # Check meta
    assert_that(resp['meta']['pagination']['page']).is_greater_than_or_equal_to(1)

    # Check data
    assert_that(resp).contains('data')
    assert_that(len(resp['data'])).is_greater_than_or_equal_to(1)

    # Check data -> store_name
    assert_that(resp['data'][0]['store_name']).contains_ignoring_case(keyword)

def test_get_stores_with_valid_filter_keyword_zero_result():
    keyword = 'ThisFilterWillBeZeroResult'

    response = r.get(f'{base_url}/api/v1/stores?keyword={keyword}')
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(200)

    # Check data
    assert_that(resp['data']).is_empty()

def test_get_stores_with_invalid_filter_keyword():
    keyword = 'in'

    response = r.get(f'{base_url}/api/v1/stores?keyword={keyword}')
    resp = response.json()

    # Check status code
    assert_that(response.status_code).is_equal_to(400)

    # Check meta
    assert_that(resp['meta']['message']).is_equal_to('at least 3 characters')

    # Check data
    assert_that(resp['data']).is_none()