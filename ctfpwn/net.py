import requests


def http_get(url):
    """
    executes regular HTTP GET request to url
    returns response body
    """
    resp = requests.get(url)
    return resp.content
