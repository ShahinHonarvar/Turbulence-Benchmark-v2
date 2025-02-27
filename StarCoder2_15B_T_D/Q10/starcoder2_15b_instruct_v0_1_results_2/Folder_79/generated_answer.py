def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 3 and i < 8 and (num % 2 == 1)]