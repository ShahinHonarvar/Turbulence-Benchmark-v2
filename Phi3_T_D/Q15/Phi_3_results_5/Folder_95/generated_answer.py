def sum_odd_ints_inclusive(int_list):
    summation = sum((int_list[82:87:2][n % 2 == 1] for n in range(3)))
    return summation