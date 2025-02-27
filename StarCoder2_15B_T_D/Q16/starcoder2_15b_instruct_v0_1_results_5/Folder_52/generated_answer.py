def sum_even_ints_inclusive(int_list):
    sum_even_ints = 0
    for i in range(28, 39):
        if int_list[i] % 2 == 0:
            sum_even_ints += int_list[i]
    return sum_even_ints