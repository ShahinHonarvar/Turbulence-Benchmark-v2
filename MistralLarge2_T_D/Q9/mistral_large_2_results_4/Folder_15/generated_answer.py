def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list[:4]) if num % 2 != 0]