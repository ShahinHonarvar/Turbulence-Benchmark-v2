def all_odd_ints_inclusive(ints_list):
    return [num for i, num in enumerate(ints_list) if i % 2 == 1 and 1 <= i <= 8]