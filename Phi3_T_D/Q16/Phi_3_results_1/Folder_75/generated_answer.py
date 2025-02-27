def sum_even_ints_inclusive(lst):
    start_index = 56
    end_index = 57
    return sum((val for val in lst[start_index:end_index + 1] if val % 2 == 0))