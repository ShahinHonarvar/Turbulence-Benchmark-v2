def sum_even_ints_inclusive(int_list):
    sum_even_ints = sum((int_list[25:60][i] for i in range(len(int_list[25:60])) if int_list[25:60][i] % 2 == 0))
    return sum_even_ints