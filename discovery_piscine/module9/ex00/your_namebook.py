

def array_of_names(person):
    name_list = []

    for f, l in person.items():
        name_list.append(f.capitalize()+" "+l.capitalize())

    return name_list

persons = {

    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"

    }

print(array_of_names(persons))
