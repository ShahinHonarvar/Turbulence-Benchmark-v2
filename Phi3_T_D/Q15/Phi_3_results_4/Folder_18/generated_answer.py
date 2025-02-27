def sum_odd_ints_inclusive(int_list):
    sum_odd = sum((int_list[i] for i in range(35, 50) if int_list[i] % 2 != 0))
    return sum_odd