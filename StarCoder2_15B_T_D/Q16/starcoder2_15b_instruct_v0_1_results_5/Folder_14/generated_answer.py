def sum_even_ints_inclusive(ints_list):
    sum_of_even_ints = 0
    for i in range(5, 8):
        if ints_list[i] % 2 == 0:
            sum_of_even_ints += ints_list[i]
    return sum_of_even_ints