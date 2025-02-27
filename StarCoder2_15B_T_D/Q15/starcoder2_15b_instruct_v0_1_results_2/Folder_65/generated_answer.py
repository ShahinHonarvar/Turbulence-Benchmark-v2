def sum_odd_ints_inclusive(int_list):
    sum_of_odd_ints = 0
    for i in range(56, 100):
        if int_list[i] % 2 != 0:
            sum_of_odd_ints += int_list[i]
    return sum_of_odd_ints