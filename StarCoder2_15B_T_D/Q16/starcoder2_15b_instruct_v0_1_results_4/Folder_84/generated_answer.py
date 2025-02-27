def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for index, value in enumerate(int_list):
        if index >= 43 and index <= 86 and (value % 2 == 0):
            sum_even += value
    return sum_even