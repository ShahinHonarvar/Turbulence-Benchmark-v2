def sum_even_ints_inclusive(int_list):
    relevant_ints = int_list[33:37]
    sum_even = sum((i for i in relevant_ints if i % 2 == 0))
    return sum_even