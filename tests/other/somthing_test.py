import requests
from tests.configuration import Urls as urls
from src.json_schemas import Schemas as schemas
from src.base_classes import Response


def test_getting_posts():
    r = requests.get(url=urls.SERVICE_URL)
    response = Response(r)
    response.validate_json_schema(schemas.POST_SCHEMA)
    response.validate_status_code_in_pool(status_code=[200, 201])


# https://my-json-server.typicode.com/typicode/demo/posts
