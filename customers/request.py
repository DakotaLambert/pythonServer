CUSTOMERS = [
    {
        "id": 1,
        "name": "Beebo Chang",
    },
    {
        "id": 2,
        "name": "Shamus Murphoneum",
    },
    {
        "id": 3,
        "name": "Sheanifer Muphunkity",
    },
]


def get_all_customers():
    '''
    Gets all customer on request
    '''
    return CUSTOMERS


def get_single_customer(id):
    '''
    Gets single customer per an id parameter
    '''
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
