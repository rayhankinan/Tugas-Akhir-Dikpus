import requests
import json

response = requests.request('GET', 'https://random-data-api.com/api/users/random_user')

file = open('DataUser.json', 'w')
json.dump(response.json(), file)
file.close()

file = open('DataUser.json', 'r')
data = json.load(file)

for key in data.keys():
    if type(data[key]) is dict:
        print(key, " : ")
        for anotherKey in data[key].keys():
            if type(data[key][anotherKey]) is dict:
                print("\t", anotherKey, " : ")
                for yetAnotherKey in data[key][anotherKey].keys():
                    print("\t\t", yetAnotherKey, " : ", data[key][anotherKey][yetAnotherKey])
            else:
                print("\t", anotherKey, " : ", data[key][anotherKey])
    else:
        print(key, " : ", data[key])

file.close()