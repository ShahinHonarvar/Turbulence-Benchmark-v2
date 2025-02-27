def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst, start=1) if i > 111 and i < 473 and (num % 2 != 0)]