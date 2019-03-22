# ctfpwn/net - network routines - HTTP request/responses handling etc. :)

import requests

hd = {
    'User-Agent': 'ctfpwn by bl4de',
    'Connection': 'Close'
}


def http_get(url, h=False):
    """
    executes regular HTTP GET request to url
    returns response body
    """
    global hd
    if h:
        hd = h
    resp = requests.get(url, headers=hd)
    return resp.content


def http_post(url, post_data, h=False):
    """
    executes HTTP POST request
    """
    global hd
    if h:
        hd = h
    resp = requests.post(url, data=post_data, headers=h)
    return resp.content


def get_http_response_header(url, header_name, h=False):
    """
    returns 'header_name' HTTP response header from the server
    """
    global hd
    if h:
        hd = h
    resp = requests.get(url, headers=hd)
    return resp.headers[header_name]


def http_headers(url, _header=""):
    """
    returns dictionary contains HTTP response headers
    {header1: value1, ...., headerN: valueN,}
    or _header, if set
    """
    resp = requests.get(url, headers=hd)
    _headers = resp.headers

    # return single _header, if set:
    if _header:
        return _headers[_header]

    # returnall headers as dict
    return _headers


def find_in_response(resp, query):
    """
    check if HTTP response contains 'to_find' string
    returns True if found, False otherwise
    """
    return True if query in resp else False
