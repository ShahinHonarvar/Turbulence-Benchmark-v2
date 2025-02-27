def sum_even_ints_inclusive(integers):
    sum = 0
    for index, value in enumerate(integers):
        if index >= 23 and index <= 23 and (value % 2 == 0):
            sum += value
    return sum