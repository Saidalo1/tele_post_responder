from os import environ


def os_environ_get(value: str):
    return environ.get(value)
