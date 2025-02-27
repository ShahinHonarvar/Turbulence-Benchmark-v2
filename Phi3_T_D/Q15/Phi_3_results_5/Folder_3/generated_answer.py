def sum_odd_ints_inclusive(int_list):
    total = 0
    for index in range(62, 93):
        if int_list[index] % 2 != 0:
            total += int_list[index]
    return total