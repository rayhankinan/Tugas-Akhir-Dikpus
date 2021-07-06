import requests

def GetData(**kwargs):
    url = "https://www.1secmail.com/api/v1/"

    for key, value in kwargs.items():
        if url == "https://www.1secmail.com/api/v1/":
            url += '?' + str(key) + '=' + str(value)
        else:
            url += "&" + str(key) + '=' + str(value)