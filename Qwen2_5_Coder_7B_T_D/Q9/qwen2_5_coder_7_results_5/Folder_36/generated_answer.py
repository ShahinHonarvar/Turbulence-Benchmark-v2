def all_odd_ints_inclusive(int_list):
    return [num for idx, num in enumerate(int_list, start=246) if idx <= 750 and num % 2 != 0]