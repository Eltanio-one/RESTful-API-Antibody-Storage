import requests
from datetime import datetime

BASE = "http://127.0.0.1:5000/"

curr_date = datetime.today().strftime('%Y-%m-%d')

# post works
response = requests.post(BASE + "antibody/1", {"marker": "CD34", "fluorophore": "APC", "supplier": "Miltenyi", "code": "12345F", "price": 242, "date": curr_date})

# get works
response = requests.get(BASE + "antibody/1")
print(response.json())

# put works
response = requests.put(BASE + "antibody/1", {"marker": "CD34", "fluorophore": "APC", "supplier": "Miltenyi", "code": "12345F", "price": 1000, "date": curr_date})

# patch works
response = requests.patch(BASE + "antibody/1", {"marker": "CD38"})

# del works
response = requests.delete(BASE + "antibody/1")

