def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 15 and i < 40 and (num % 2 == 1)]