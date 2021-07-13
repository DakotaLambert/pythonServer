ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"

    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"

    }
]

# Function with a single parameter


def get_all_animals():
    '''
    gets all animals in request
    '''
    return ANIMALS


def get_single_animal(id):
    '''
    used for singling out an animalByID
    '''
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    '''
    posts the new animal information with an id + 1 to the last indexed id
    '''

    max_id = ANIMALS[-1]['id']

    new_id = max_id + 1

    animal["id"] = new_id

    ANIMALS.append(animal)

    return animal


def delete_animal(id):
    '''
    Deletes the animal object that matches the ID entered in param
    '''
    animal_index = -1

    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index

    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    '''
    updates animal information
    '''
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break
