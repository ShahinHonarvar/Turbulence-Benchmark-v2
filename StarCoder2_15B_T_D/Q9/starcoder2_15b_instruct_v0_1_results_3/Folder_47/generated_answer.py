def all_odd_ints_inclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 37 and i <= 76 and (num % 2 == 1)]