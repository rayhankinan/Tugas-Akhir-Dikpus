import requests

response = requests.request('GET', 'https://random-data-api.com/api/users/random_user')

data = response.json()

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