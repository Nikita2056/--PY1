list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_numbers = list_numbers[0];
max_index = 0;
for i in range(20):
    if list_numbers[i] > max_numbers:
        max_numbers = list_numbers[i];
        max_index = i;
list_numbers[-1], list_numbers[max_index] =  list_numbers[max_index], list_numbers[-1];
print(list_numbers)
