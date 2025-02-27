def sum_even_ints_inclusive(ints_list):
    sum_even = 0
    for i in range(5, 8):
        if ints_list[i] % 2 == 0:
            sum_even += ints_list[i]
    return sum_even