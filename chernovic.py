# class Model(BaseModel, extra=Extra.forbid):
#     a: str
#
#
# class Post(BaseModel):  # Set the structure of the object.
#     id: int
#     title: str
#
#
# item = {'id': 1, 'title': 'Post 1'}
# Post(id=1, title='Post 1')
#
# try:
#     Model(a='spam')
#     print("OK")
# except ValidationError as e:
#     print(e)
#
# try:
#     Model(a='spam')
#     print("OK")
# except ValidationError as e:
#     print(e)
#     """
#     1 validation error for Model
#     b
#       extra fields not permitted (type=value_error.extra)
#     """
#
# res = requests.get(urls.GOREST_USERS_URL)
# r = Response(res)
# print(r.__str__())
#
#
# def get_response():
#     res = requests.get(urls.GOREST_USERS_URL)
#     print(res.json())


# class Counter:
#     def __init__(self):
#         self.value = 0
#
#     def new_value(self):
#         self.value += 1
#         return self.value
#
#     def reset(self):
#         self.value = 0
#         return self.value
#
#
# s = 'kgkjhlkhlkyuiuolhlkgkh'
#
#
# def count_string(s):
#     counter_1 = Counter()
#     return [counter_1.new_value() for i in s][:-2:-1]
#
#
# print(count_string(s))
#

car = {
    "id": 1,
    "mark": "Toyota",
    "model": "Camry",
    "made_at": "2020-07-21",
    "paid_for_parking_until": "2025-07-18",
    "VIN": "STR134562ER777",
    "status": "ACTIVE",
    "detailed_information": {
        "technical": {
            "body": "saloon",
            "color": "gray",
            "weight": 1200,
            "photo": "https://gorest.co.in/public/v1/users?page=2",
            "uuid": "124354kku-sr6790-817426-69876rv-8769708"
            },
        "owners": [{
            "name": "Wolf Kats",
            "card_number": "12345678910",
            "email": "wolf_kats@gmail.com"
            }]
        }
    }