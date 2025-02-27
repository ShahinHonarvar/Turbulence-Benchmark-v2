def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(64, 67):
        if int_list[i] % 2 == 1:
            sum += int_list[i]
    return sum