def sum_even_ints_inclusive(lst):
    if len(lst) < 7:
        return 0
    sum_even = 0
    for i in range(7):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even