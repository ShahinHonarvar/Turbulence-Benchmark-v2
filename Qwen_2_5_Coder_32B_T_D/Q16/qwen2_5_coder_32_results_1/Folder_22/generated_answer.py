def sum_even_ints_inclusive(int_list):
    if len(int_list) < 42:
        return 0
    else:
        return sum([x for x in int_list[40:42] if x % 2 == 0])