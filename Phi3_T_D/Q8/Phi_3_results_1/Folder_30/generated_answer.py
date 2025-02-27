def all_even_ints_exclusive(lst):
    return [value for index, value in enumerate(lst) if index in range(86, 90) and value % 2 == 0]