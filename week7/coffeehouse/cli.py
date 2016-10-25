import requests

counter = 0
while True:
    json_result = requests.get("http://localhost:8000/specials/").json()
    print(counter)
    counter += 1
    for special in json_result:
        print(special["name"])
        print(special["price"])
        print(special["description"])
        print("*" * 80)
