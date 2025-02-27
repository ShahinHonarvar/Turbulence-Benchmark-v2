def all_odd_ints_inclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 31 <= idx <= 72 and num % 2 != 0]