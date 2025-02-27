def sum_even_ints_inclusive(int_list):
    total = 0
    for i in range(21, 98):
        if int_list[i] % 2 == 0:
            total += int_list[i]
    return total