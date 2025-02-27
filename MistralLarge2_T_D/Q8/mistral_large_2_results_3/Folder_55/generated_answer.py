def all_even_ints_exclusive(lst):
    return [num for index, num in enumerate(lst) if index > 0 and index < 10 and (num % 2 == 0)]