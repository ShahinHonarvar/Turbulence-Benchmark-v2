def all_odd_ints_inclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 6 and i <= 8 and (num % 2 == 1)]