def sum_odd_ints_inclusive(int_list):
    total = sum((num for num in int_list[74:96] if num % 2 != 0))
    return total