def sum_odd_ints_inclusive(int_list):
    result = sum((num for num in int_list[15:40] if num % 2 != 0))
    return result