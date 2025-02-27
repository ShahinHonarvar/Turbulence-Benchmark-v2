def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if num % 2 != 0 and i in range(4, 9)]