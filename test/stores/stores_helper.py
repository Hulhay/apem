from utils.contant import STORE_CONSTANTS

def get_keyword():
    return STORE_CONSTANTS['valid_keyword']

def get_not_found_keyword():
    return STORE_CONSTANTS['not_found_keyword']

def get_invalid_keyword():
    return STORE_CONSTANTS['lt_3char_keyword']