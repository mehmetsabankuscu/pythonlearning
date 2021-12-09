import json


# # # # # dict
# person = {"name":"Ali","languages":["python","C#"]}

# # result = person["name"]
# # result=person["languages"]
# # result=person["languages"][1]

# print(result)

# person_string = '{"name":"Ali","languages":["python","C#"]}'

# JSON string to Dict
# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]


# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



## Dict to JSON string
person_dict =  {
    "name":"ali",
    "languages":["python","C#"]
}


# result =json.dumps(person_dict)

# print(type(result))


# with open ("person.json","w") as f:
#     json.dump(person_dict, f)



