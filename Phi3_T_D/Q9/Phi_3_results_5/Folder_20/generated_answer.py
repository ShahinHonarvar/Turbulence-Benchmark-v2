def all_odd_ints_inclusive(lst):
    start, end = (56, 66)
    return [num for num in lst[start:end + 1] if num % 2 != 0]