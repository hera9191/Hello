import requests


def hello_world() -> str:
    return 'Hello World!'


def hello_world_wiki() -> str:
    with requests.Session() as s:
        resp = s.get("https://cs.wikipedia.org/wiki/Hello_world")
        text = resp.text
    return text
