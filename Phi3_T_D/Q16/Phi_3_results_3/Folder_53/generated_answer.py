def sum_even_ints_inclusive(lst):
    return sum(lst[111:112]) if lst[111:112].count(lst[111:112][0]) % 2 == 0 else 0