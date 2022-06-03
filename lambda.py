people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "hermione", "house": "gryffindor"},
    {"name": "ginny", "house": "ravenclaw"},
    {"name": "dobby", "house": "ravenclaw"}
]


people.sort(key=lambda person: person["name"])
print(people)