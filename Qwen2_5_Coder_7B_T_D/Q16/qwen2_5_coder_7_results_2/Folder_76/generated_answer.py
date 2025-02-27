def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if 686 <= i <= 987 and x % 2 == 0))