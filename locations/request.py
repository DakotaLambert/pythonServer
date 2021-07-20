import sqlite3
import json

from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def get_all_locations():
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
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)


def get_single_location(id):
    '''
    used for getting and single location
    '''
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location


def create_location(location):
    '''
    posts the new animal information with an id + 1 to the last indexed id
    '''

    max_id = LOCATIONS[-1]['id']

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location


def delete_location(id):
    """[summary]

    Args:
        id ([type]): [description]
    """
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))


def update_location(id, new_location):
    '''
    updates location information
    '''
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
