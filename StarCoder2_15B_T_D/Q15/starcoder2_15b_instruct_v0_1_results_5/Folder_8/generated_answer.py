def sum_odd_ints_inclusive(lst):
    sum_odd_ints = 0
    for i in range(23, len(lst)):
        if lst[i] % 2 != 0:
            sum_odd_ints += lst[i]
    return sum_odd_ints