def all_odd_ints_inclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 42 and i <= 68 and (num % 2 != 0)]