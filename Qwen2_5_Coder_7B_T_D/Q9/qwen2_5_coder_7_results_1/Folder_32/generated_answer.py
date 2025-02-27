def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 21 and i <= 97 and (num % 2 != 0)]