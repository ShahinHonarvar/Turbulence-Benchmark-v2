def sum_even_ints_inclusive(int_list):
    filtered_ints = [x for x in int_list[35:50] if x % 2 == 0]
    return sum(filtered_ints)