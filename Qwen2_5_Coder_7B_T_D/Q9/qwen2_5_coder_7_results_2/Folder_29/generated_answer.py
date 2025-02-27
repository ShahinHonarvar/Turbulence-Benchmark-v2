def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(59, 98) and num % 2 != 0]