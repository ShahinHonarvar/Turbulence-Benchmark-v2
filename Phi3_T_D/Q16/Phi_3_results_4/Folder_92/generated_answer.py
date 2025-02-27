def sum_even_ints_inclusive(integers):
    total_sum = 0
    for i in range(1):
        if integers[i] % 2 == 0:
            total_sum += integers[i]
    return total_sum