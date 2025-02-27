def sum_odd_ints_inclusive(int_list):
    result = 0
    for i in range(4, 5):
        if int_list[i] % 2 == 1:
            result += int_list[i]
    return result