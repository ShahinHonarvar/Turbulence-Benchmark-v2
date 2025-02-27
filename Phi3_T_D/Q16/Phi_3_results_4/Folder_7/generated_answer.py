def sum_even_ints_inclusive(int_list):
    start, end = (661, 924)
    return sum([x for i, x in enumerate(int_list[start:end + 1], start) if x % 2 == 0])