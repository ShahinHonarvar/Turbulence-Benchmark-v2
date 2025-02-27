def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for _, value in enumerate(int_list[26:53]):
        if value % 2 == 0:
            even_sum += value
    return even_sum