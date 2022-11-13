import random

def get_random_password() -> str:
    list_ = random.sample(alfavit, n)
    str_ = ''
    for item in list_:
        str_ += item
    return str_
alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
n = 8
print(get_random_password())
