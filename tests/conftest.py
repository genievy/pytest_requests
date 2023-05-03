import pytest
import requests
from tests.configuration import Urls as urls
from src.base_classes import Response


@pytest.fixture(scope='function')
def res_object():
    response = requests.get(urls.GOREST_GET_USER)
    return Response(response)

