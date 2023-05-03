import pytest


@pytest.fixture
def input_value():
    input = 39
    print('input = ', input)
    return input
