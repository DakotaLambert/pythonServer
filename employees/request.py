EMPLOYEES = [
    {
        "id": 1,
        "name": "Bjorn Tfyuk",
        "location": "Nashville North"
    },
    {
        "id": 2,
        "name": "Shamus Murphoneum",
        "location": "Nashville South"
    },
    {
        "id": 3,
        "name": "Mizgog Manchuteries",
        "location": "Nashville South"
    },
]


def get_all_employees():
    '''
    Gets all employees on request
    '''
    return EMPLOYEES


def get_single_employee(id):
    '''
    Gets single employee per an id parameter
    '''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
