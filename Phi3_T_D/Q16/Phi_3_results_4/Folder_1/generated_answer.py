def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(31, 73):
        if isinstance(lst[i], int) and lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum