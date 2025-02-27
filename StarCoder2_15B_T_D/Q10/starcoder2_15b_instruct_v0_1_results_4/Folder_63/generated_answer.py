def all_odd_ints_exclusive(ints):
    return [num for i, num in enumerate(ints) if i >= 38 and i < 52 and (num % 2 == 1)]