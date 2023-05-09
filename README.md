# RESTful_API_Antibody_Storage
A RESTful API created using python, flask, flask_restful and SQLAlchemy. The aim of this API was to practice both creating a RESTful API, and to further my understanding of RESTful APIs. The database stores information on antibody orders that can will be placed, and keeps a record of the date of when the antibody was ordered.

Below I have detailed the different files that are included in this repo, and explain what each part of each file does.

# parsers.py
This python file contains reqparse RequestParsers from the flask_restful library that have the relevant arguments from the Antibody class added to each. I have created three different parsers for POST, PUT and PATCH HTTP requests, as each of these have different necessities regarding the requirements of fields when sending the relevant request. These are then imported into main.py to be used when requesting to parse the arguments provided in test.py (this can also be done through the command line).

# test.py
This python file contains code that tests each of the HTTP request functions that the API allows; GET, POST, PUT, PATCH and DELETE. I have also included datetime from the datetime library to generate the current date so that when users send either a POST, PUT or PATCH request, the date is automatically generated to minimise error and enable accurate tracking of order dates.

# requirements.txt
This text file contains all libraries required for the running of the API.

# database.db
This database ontains the data stored from HTTP requests.

# main.py
This is the main file where the API is configured and HTTP request functions are defined. The file itself is commented out with the specific action behind each section of code, but below I have included a general description of main.py:

A flask application and flask_restful API are initialised, before configuring the app to be linked to a SQLAlchemy database to store data that is generated through HTTP requests. The AntibodyModel is created and houses the various attributes that each antibody entry can have. Next, the Antibody resource is created for the API, which includes functions that handle GET, POST, PUT, PATCH and DELETE HTTP requests. Each of these functions is wrapped in the marshal_with decorator, that uses the resource_fields dictionary to format the result that is generated before passing the data base to test.py or the command line (wherever is executing the request). the Antibody resource is then added to the flask_restful API, and the API is run in debug mode so that any updates to the code would be reflected in the command-line, and refreshing is not necessary.

Any questions or bugs, please drop me a message!
