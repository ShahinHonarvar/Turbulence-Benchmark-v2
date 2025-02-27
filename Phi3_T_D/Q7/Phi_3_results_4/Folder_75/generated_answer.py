def all_even_ints_inclusive(lst):
    start_index, end_index = (56, 57)
    return [num for num in lst[start_index:end_index + 1] if num % 2 == 0]