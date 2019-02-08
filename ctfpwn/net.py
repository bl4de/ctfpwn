import requests

headers = {
    'User-Agent': 'ctfpwn by bl4de',
    'Connection': 'Close'
}


def http_get(url):
    """
    executes regular HTTP GET request to url
    returns response body
    """
    resp = requests.get(url, headers=headers)
    return resp.content


def http_headers(url, _header=""):
    """
    returns dictionary contains HTTP response headers
    {header1: value1, ...., headerN: valueN,}
    or _header, if set
    """
    resp = requests.get(url, headers=headers)
    _headers = resp.headers

    # return single _header, if set:
    if _header:
        return _headers[_header]

    # returnall headers as dict
    return _headers


def find_in_response(url, to_find):
    """
    check if HTTP response contains 'to_find' string
    returns True if found, False otherwise
    """
    return True if to_find in http_get(url) else False
