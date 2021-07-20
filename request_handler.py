from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from customers.request import create_customer, get_single_customer, get_all_customers, delete_customer, update_customer, get_customers_by_email
from employees.request import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from locations.request import get_all_locations, get_single_location, create_location, delete_location, update_location
from animals import get_all_animals, get_single_animal, create_animal
from animals import delete_animal
from animals import update_animal
# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    '''
    This class handles all base HTTP requests
    '''

    def parse_url(self, path):
        '''
        parses URL
        '''
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:

            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return (resource, key, value)
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    # Here's a class function

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed #pylint: disable=unbalanced-tuple-unpacking

            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                else:
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers}"
            elif resource == "locations":
                if id is not None:
                    response = f"{get_single_location(id)}"
                else:
                    response = f"{get_all_locations()}"
            elif resource == "employees":
                if id is not None:
                    response = f"{get_single_employee(id)}"
                else:
                    response = f"{get_all_employees()}"

        elif len(parsed) == 3:
            (resource, key, value) = parsed

            if key == "email" and resource == "customers":
                response = get_customers_by_email(value)

        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path) #pylint: disable=unbalanced-tuple-unpacking

        new_animal = None
        new_location = None
        new_customer = None
        new_employee = None

        if resource == "animals":
            new_animal = create_animal(post_body)

        if resource == "locations":
            new_location = create_location(post_body)

        if resource == "customers":
            new_customer = create_customer(post_body)

        if resource == "employees":
            new_employee = create_employee(post_body)

        self.wfile.write(f"{new_animal}".encode())
        self.wfile.write(f"{new_location}".encode())
        self.wfile.write(f"{new_customer}".encode())
        self.wfile.write(f"{new_employee}".encode())

    def do_DELETE(self):
        '''
        handles DELETE requests to the server
        '''
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path) #pylint: disable=unbalanced-tuple-unpacking

        if resource == "animals":
            delete_animal(id)

        if resource == "locations":
            delete_location(id)

        if resource == "customers":
            delete_customer(id)

        if resource == "employees":
            delete_employee(id)

        self.wfile.write("".encode())
    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path) #pylint: disable=unbalanced-tuple-unpacking

        if resource == "animals":
            update_animal(id, post_body)

        if resource == "locations":
            update_location(id, post_body)

        if resource == "customers":
            update_customer(id, post_body)

        if resource == "employees":
            update_employee(id, post_body)

        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
