def all_even_ints_inclusive(lst):
    start_index = 73
    end_index = 73
    return [x for x in lst[start_index:end_index + 1] if x % 2 == 0]