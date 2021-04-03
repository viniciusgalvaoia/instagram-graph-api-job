import requests


def get_token():
    token = ""
    return token


def build_url(base, node, parameters):
    return f"{base}{node}{parameters}"


def request_data(url):
    response = requests.get(url)
    data = response.json()
    return data
