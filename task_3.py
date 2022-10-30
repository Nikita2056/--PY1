def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    result = []
    i = 0
    if index == None:
        index = len(list_)-1
    for item in list_:
        if i == index:
            i += 1
            continue
        i += 1
        result.append(item)
    return result

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
