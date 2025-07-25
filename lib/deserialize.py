# lib/deserialize.py

from marshmallow import Schema, fields
from pprint import pprint

# schema

class HamsterSchema(Schema):
     name = fields.Str()
     breed = fields.Str()
     dob = fields.Date()

hamster_schema = HamsterSchema()

hamster_dict = {"name": "Fluffernutter", "breed": "Roborovski", "dob": "2014-08-11"}
result = hamster_schema.load(hamster_dict)
print(type(result))
pprint(result)

hamster_json = '{"name": "Wiggles", "breed": "Siberian", "dob": "2020-01-30"}'
result_2 = hamster_schema.loads(hamster_json)
print(type(result_2))
pprint(result_2)