def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 62 and i <= 99 and (num % 2 != 0)]