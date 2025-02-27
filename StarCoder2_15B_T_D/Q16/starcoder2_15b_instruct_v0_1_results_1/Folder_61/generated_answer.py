def sum_even_ints_inclusive(int_list):
    return sum([n for n in int_list if n % 2 == 0 and int_list.index(n) in range(8)])