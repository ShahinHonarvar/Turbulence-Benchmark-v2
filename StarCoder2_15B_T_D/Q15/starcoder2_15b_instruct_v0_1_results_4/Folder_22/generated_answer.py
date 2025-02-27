def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(40, 42):
        if lst[i] % 2 == 1:
            sum_odd += lst[i]
    return sum_odd