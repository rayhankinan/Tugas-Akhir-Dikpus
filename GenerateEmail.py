import requests

def GetData(**kwargs):
    url = "https://www.1secmail.com/api/v1/"

    for key, value in kwargs.items():
        if url == "https://www.1secmail.com/api/v1/":
            url += '?' + str(key) + '=' + str(value)
        else:
            url += "&" + str(key) + '=' + str(value)
    
    response = requests.request("GET", url)

    data = response.json()

    return data

if __name__ == "__main__":
    pass