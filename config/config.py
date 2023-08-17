import os
import dotenv
import faker

dotenv.load_dotenv()

def get_base_url():
    return os.environ['BASE_URL_TESTING']

def init_faker():
    return faker.Faker()