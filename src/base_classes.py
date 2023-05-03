from jsonschema import validate


class Response:

    def __init__(self, response):
        self.parsed_object = None
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code
        self.__setattr__('wrong_status_code', str)
        # self.wrong_status_code = 'Reseived status code is not equal to expected.'
        # self.wrong_number_elements = 'Wrong number of elements in response.'

    def wrong_status_code(self):
        return \
            f"\nStatus code: {self.response_status_code} \n" \
            f"Request url: {self.response.url} \n" \
            f"Reseived status code is not equal to expected"

    """This is an example of using jsonschema to validate data in a response"""
    def validate_json_schema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def validate_pydentic_schema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.parse_obj(self.response_json)
        return self

    def validate_status_code_in_pool(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self.wrong_status_code
        else:
            assert self.response_status_code == status_code, self.wrong_status_code
        return self

    def validate_status_code(self, status_code):
        assert self.response_status_code == status_code, self.wrong_status_code
        return self

    def get_parsed_object(self):
        return self.parsed_object()
