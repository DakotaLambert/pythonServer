
import sqlite3
import json

from models import Employee

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
    """[summary]

    Returns:
        [type]: [description]
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


def get_single_employee(id):
    '''
    Gets single employee per an id parameter
    '''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    '''
    posts the new animal information with an id + 1 to the last indexed id
    '''

    max_id = EMPLOYEES[-1]['id']

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee(id):
    """[summary]

    Args:
        id ([type]): [description]
    """
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))


def update_employee(id, new_employee):
    '''
    updates animal information
    '''
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
        