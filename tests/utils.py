import random
import string

_data = string.ascii_letters + string.digits


def get_random_charset(length):
    charset = ''
    for _ in range(length):
        random_int = random.randint(0, len(_data)-1)
        char = _data[random_int]
        charset += char
    return charset
