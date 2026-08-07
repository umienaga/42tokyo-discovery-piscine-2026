


def find_the_redheads(person):
    name_list = []

    name_list = list(filter(lambda name: person[name] == "red", person))

    return name_list

dupont_family = {

    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"

}


print(find_the_redheads(dupont_family))




