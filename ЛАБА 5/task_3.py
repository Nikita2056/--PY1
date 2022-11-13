from random import randint
def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_)< count:
        rand = randint(min, max)
        if (list_.count(rand)):
            continue
        else:
            list_.append(rand)
    return list_
count = 15
min = -10
max = 10
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
