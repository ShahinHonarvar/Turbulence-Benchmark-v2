def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 13 <= i < 76 and num % 2 == 1]