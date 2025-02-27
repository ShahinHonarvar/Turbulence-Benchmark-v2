def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(40, 81):
        if i < len(int_list) and int_list[i] % 2 != 0:
            total += int_list[i]
    return total