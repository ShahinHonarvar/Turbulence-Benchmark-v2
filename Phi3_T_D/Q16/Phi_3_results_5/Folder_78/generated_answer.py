def sum_even_ints_inclusive(int_list):
    return sum(int_list[43:52]) - sum(filter(lambda n: n % 2 != 0, int_list[43:52]))