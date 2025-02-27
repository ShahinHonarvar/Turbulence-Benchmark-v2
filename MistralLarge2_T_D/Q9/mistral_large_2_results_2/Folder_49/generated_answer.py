def all_odd_ints_inclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 80 <= idx <= 200 and num % 2 != 0]