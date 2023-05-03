from src.pydentic_schemas import Cars
from examples import car


def test_pydentic_object():
    car_1 = Cars.parse_obj(car)
    print(car_1.detailed_information)
    # res_object.validate_pydentic_schema(Cars)
    print(car_1.schema_json())
