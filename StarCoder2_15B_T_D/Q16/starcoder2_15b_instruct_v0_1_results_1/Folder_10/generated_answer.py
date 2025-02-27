def sum_even_ints_inclusive(list_of_ints):
    sum = 0
    for index in range(25, 60):
        if index % 2 == 0:
            sum += list_of_ints[index]
    return sum