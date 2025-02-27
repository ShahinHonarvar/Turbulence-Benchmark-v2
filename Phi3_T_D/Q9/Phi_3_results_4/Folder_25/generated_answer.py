def all_odd_ints_inclusive(lst):
    start_index = 29
    end_index = 93
    return [num for num in lst[start_index:end_index + 1] if num % 2 != 0]