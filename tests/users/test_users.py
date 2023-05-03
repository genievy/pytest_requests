from src.pydentic_schemas import GorestGetUsers
from src.pydentic_schemas import Cars
import pytest


@pytest.mark.users
def test_getting_users_list(res_object):
    res_object.validate_status_code(200).validate_pydentic_schema(GorestGetUsers)


# @pytest.mark.xfail
# @pytest.mark.parametrize('a, b', [(2, 3), (3, 3), (7, 7)])
def test_equal(a, b):
    assert a == b, "b is not equal a"



