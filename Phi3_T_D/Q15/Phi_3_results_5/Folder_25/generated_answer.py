def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(29, 94):
        if int_list[i] % 2 != 0:
            total += int_list[i]
    return total